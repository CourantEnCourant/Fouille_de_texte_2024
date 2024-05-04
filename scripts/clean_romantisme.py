from create_corpus import clean_poem
from pathlib import Path
from typing import List


def get_txt(input_folder: Path) -> List[Path]:
    # Recursion func that takes in a folder of corpus, returns paths of all txt files
    list_txt = []
    if input_folder.is_file():
        if input_folder.suffix == '.txt':
            list_txt.append(input_folder)
    elif input_folder.is_dir():
        for next_level in input_folder.iterdir():
            list_txt.extend(get_txt(next_level))

    return list_txt


def main():
    list_txt = get_txt(Path('../corpus_fouille/corpus_traite'))

    count = 1
    for text in list_txt:
        with open(text, 'r') as old_text:
            new_text = clean_poem(old_text.read())
            with open(f'../corpus/clean/romantisme/poem{count}.txt', 'w') as new_file:
                new_file.write(new_text)
        count += 1


if __name__ == '__main__':
    main()