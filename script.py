from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1").get_text(strip=True)
liste_ingredient = soup.find('div', class_='ingredients').text
preparation = soup.find('table', class_='preparation').text
description = soup.find('p', class_='description').text


print("Titre de la page HTML : ", titre_h1)
print("Liste des ingredients : ", liste_ingredient)
print("Preparation : ", preparation)
print("description : ", description)






