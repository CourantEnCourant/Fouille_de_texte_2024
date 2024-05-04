from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from typing import List
import re


def clean_poem(raw_poem : str) -> str:
    # Clean a poem
    note_symbols = r'[\[\]0-9]' # These are notes, like [1]...
    poem_cleaned = re.sub(note_symbols, '', raw_poem.lower()) # Clean notes
    poem_cleaned = ' '.join(poem_cleaned.split()) # One poem per line

    return poem_cleaned


def get_files(input_folder: Path) -> List[Path]:
    # Recursion func that takes in a folder of corpus, returns paths of all html files
    list_htmls = []
    if input_folder.is_file():
        if input_folder.suffix == '.html':
            absolute_path = input_folder.absolute() # Absolute path because it works better with selenium driver
            list_htmls.append(absolute_path)
    elif input_folder.is_dir():
        for next_level in input_folder.iterdir():
            list_htmls.extend(get_files(next_level))

    return list_htmls


def get_poems(driver, file_html) -> List[str]:
    # Get poems from a wikisource html file
    clean_poems = []
    driver.get(f'file://{file_html}')
    raw_poems = driver.find_elements(By.XPATH, '//div[@class="poem" or @class="poem1"]') # "poem1" is for La Fontaine
    print(f'Number of poem in {file_html}: {len(raw_poems)}.') # To verify if this html file is usable.
    raw_poems = raw_poems[:30] # For each html file, only 30 poems.

    for raw_poem in raw_poems:
        raw_poem = raw_poem.text
        poem_cleaned = clean_poem(raw_poem)
        clean_poems.append(poem_cleaned)

    return clean_poems


def main(input_folder : Path, period : str):
    # Create corpus of a certain period, each poem a file. For each html file, only 30 poems.
    html_paths = get_files(input_folder)

    count_file = 1
    driver = webdriver.Chrome()

    for html in html_paths:
        poems = get_poems(driver, html)
        for poem in poems:
            with open(f'../corpus/clean/{period}/poem_{count_file}.txt', 'w', encoding='utf-8') as poem_file:
                poem_file.write(poem)
                count_file += 1


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create corpus of a specific period.')
    parser.add_argument('input_folder', type=Path, help='Folder that contains html files of a specific period.')
    parser.add_argument('period', choices=['renaissance', 'classicisme', 'romantisme'], help='The period you want to choose.')

    args = parser.parse_args()

    main(
        input_folder=args.input_folder,
        period=args.period
    )
