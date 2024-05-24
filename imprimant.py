import requests
from bs4 import BeautifulSoup
import time



def get_All_Page():
    page_number = 1
    urls = []
    for i in range(2):
        lien = f"https://www.mytek.tn/impression/imprimantes/imprimante-a-reservoir-integre.html?p={page_number}"
        page_number += 1
        urls.append(lien)
    return urls


def gratter_imprimantes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Cookie': 'section_data_ids={%22customer%22:1712927642%2C%22cart%22:1712927642}; _fbp=fb.1.1712923054261.1619969028; _ga=GA1.1.2119425263.1712923054; _ga_7ZZBB6THYG=GS1.1.1712923054.1.1.1712927641.43.0.0; _gcl_au=1.1.589267857.1712923054; STUID=ec43d5ec-e86f-ff47-b00d-cf9b1e2566d9; mage-cache-sessid=true; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; product_data_storage={}; recently_compared_product={}; recently_compared_product_previous={}; recently_viewed_product={}; recently_viewed_product_previous={}; STVID=14dd27a0-a668-9192-dcbb-5dcf737660f9; form_key=PxWJlovBHK7O0X32; cf_chl_3=; cf_clearance=8xq9hcZ7GnS9u9NrFr1gcI.9ol_10_n2NygDuwlA7e0-1712923053-1.0.1.1-z8KYp_S5rD9iRDc5fruLFFxnmUBIYPQHb547dnXt40bZfGL5EusS2ugtkKV7Z1Ug2JkvZtXxtlmaLSBsUYcGmw'

    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Vérifier si la requête a réussi
    except requests.HTTPError as e:
        print(f"Erreur HTTP lors de la récupération de {url}: {e}")
        return

    soup = BeautifulSoup(r.content, "html.parser")
    imprimantes = soup.findAll("li", class_="item product product-item")
    print(imprimantes)
    for impr in imprimantes:
        try:
            nom = impr.find("strong", class_="product name product-item-name").text.strip()
        except AttributeError as e:
            nom = ""
        try:
            reference = impr.find("div", class_="skuDesktop").text.strip()
        except AttributeError as e:
            reference = ""

        try:
            description = impr.find("div", class_="product description product-item-description").text.strip()
        except AttributeError as e:
            description = ""
        try:
            prix = impr.find("div", class_="price-box price-final_price").text.strip()
        except AttributeError as e:
            prix = ""
        chemin = r"/Users/shaik1/Desktop/Formation_dev_cy/imprimantes.txt"
        with open(chemin, "a") as fichier:
            fichier.write(f"{nom}\n")
            fichier.write(f"{reference}\n")
            fichier.write(f"{description}\n")
            fichier.write(f"{prix}\n\n")

    time.sleep(1)


def grater_toutes_les_imprimantes():
    pages = get_All_Page()
    for page in pages:
        gratter_imprimantes(url=page)
        print(f"on scrappe {page}")


gratter_imprimantes(
    "https://www.mytek.tn/impression/imprimantes/imprimante-a-reservoir-integre.html"
)
grater_toutes_les_imprimantes()
