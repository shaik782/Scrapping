"""import requests
from bs4 import BeautifulSoup

def get_avocats_info(url):
    # Faire la requête HTTP
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ouvrir un fichier en mode écriture
        with open('avocats.txt', 'w', encoding='utf-8') as f:
            # Trouver tous les éléments contenant les informations des avocats
            avocats = soup.find_all('div', class_='callout secondary annuaire-single')
            print(avocats)
            
            # Parcourir chaque avocat et écrire les informations dans le fichier
            for avocat in avocats:
                nom_prenom = avocat.find('h3', class_='nom-prenom').text.strip()
                nom, prenom = nom_prenom.split(' ', 1)
                adresse = avocat.find('span', class_='adresse').text.strip()
                telephone = avocat.find('span', class_='telephone').text.strip()
                email = avocat.find('span', class_='email').text.strip().split(':')[-1].strip()
                
                # Écrire les informations dans le fichier
                f.write("Nom: {}\n".format(nom))
                f.write("Prénom: {}\n".format(prenom))
                f.write("Téléphone: {}\n".format(telephone))
                f.write("Adresse: {}\n".format(adresse))
                f.write("Email: {}\n".format(email))
                f.write("\n")

# URL du site
url = 'https://www.barreaudenice.com/annuaire/avocats/'

# Appeler la fonction pour récupérer les informations des avocats
get_avocats_info(url)

print("Les informations des avocats ont été enregistrées dans avocats.txt.")"""

import requests
from bs4 import BeautifulSoup
import re


def get_All_Page():
    page_number = 1
    urls = []
    for i in range(104):
        lien = (
            f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        )
        page_number += 1
        urls.append(lien)
    return urls


def gratter_avocat(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    avocats = soup.findAll("div", class_="callout secondary annuaire-single")

    for avocat in avocats:
        try:
            nom = avocat.find("h3").text.strip()
        except AttributeError as e:
            nom = ""
        try:
            adresse = avocat.find("span", class_="adresse").text.strip()
            adresse_finale = re.sub(r"\s+", " ", adresse)
        except AttributeError as e:
            adresse_finale = ""

        try:
            tel = avocat.find("span", class_="telephone").text.strip()
        except AttributeError as e:
            tel = ""
        try:
            email = avocat.find("span", class_="email").a.text.strip()
        except AttributeError as e:
            email = ""
        chemin = r"/Users/shaik1/Desktop/Formation_dev_cy/avocats.txt"
        with open(chemin, "a") as fichier:
            fichier.write(f"{nom}\n")
            fichier.write(f"{adresse_finale}\n")
            fichier.write(f"{tel}\n")
            fichier.write(f"{email}\n\n")


def grater_tous_les_avocats():
    pages = get_All_Page()
    for page in pages:
        gratter_avocat(url=page)
        print(f"on scrappe {page}")


grater_tous_les_avocats()
