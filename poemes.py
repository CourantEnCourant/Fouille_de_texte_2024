import requests
from bs4 import BeautifulSoup

urls = [
    "https://fr.wikisource.org/wiki/Les_Contemplations/«_Demain,_dès_l’aube,_à_l’heure_où_blanchit_la_campagne_»",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/À_une_femme",
    "https://fr.wikisource.org/wiki/Les_Orientales/Attente",
    "https://fr.wikisource.org/wiki/Les_Orientales/Canaris",
    "https://fr.wikisource.org/wiki/À_Lydie_(Hugo)",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/Avril_–_À_Louis_B.",
    "https://fr.wikisource.org/wiki/Les_Rayons_et_les_Ombres/Sur_un_homme_populaire",
    "https://fr.wikisource.org/wiki/Les_Rayons_et_les_Ombres/Guitare",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/À_M._David,_statuaire",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/À_M._de_Lamartine",
    "https://fr.wikisource.org/wiki/Odes_et_Ballades/À_M._de_Chateaubriand",
    "https://fr.wikisource.org/wiki/Les_Contemplations/À_la_mère_de_l’enfant_mort",
    "https://fr.wikisource.org/wiki/Les_Contemplations/À_M._Froment_Meurice",
    "https://fr.wikisource.org/wiki/Les_Contemplations/À_ma_fille",
    "https://fr.wikisource.org/wiki/Les_Contemplations/À_un_poëte_aveugle",
    "https://fr.wikisource.org/wiki/Odes_et_Ballades/Le_Chant_de_l’arène",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/À_un_riche",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/«_Regardez._Les_enfants_se_sont_assis_en_rond_»",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/«_Regardez._Les_enfants_se_sont_assis_en_rond_»",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/«_Dans_ce_jardin_antique…_»",
    "https://fr.wikisource.org/wiki/Les_Voix_intérieures/À_des_oiseaux_envolés",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/«_Ce_siècle_avait_deux_ans_!_»",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/Envoi_des_Feuilles_d’Automne",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/«_L’aurore_s’allume_»",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/«_Hier,_la_nuit_d’été,_qui_nous_prêtait_ses_voiles_»",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/Nouvelle_chanson_sur_un_vieil_air",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/«_Oh_!_pour_remplir_de_moi_ta_rêveuse_pensée_»",
    "https://fr.wikisource.org/wiki/Les_Chants_du_crépuscule/«_Puisque_nos_heures_sont_remplies_»",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/Dicté_en_présence_du_glacier_du_Rhône",
    "https://fr.wikisource.org/wiki/Les_Feuilles_d’automne/À_un_voyageur"
]
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    poem_container = soup.find(id='mw-content-text')

    if poem_container:
        poem_text = poem_container.get_text(strip=True)
        
        print(poem_text)
        print("_" * 30 + "\n")  
    else:
        print("Poème non trouvé pour l'URL:", url)
