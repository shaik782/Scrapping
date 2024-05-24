# Projet de Scrapping - Liste des Avocats

## Description

Ce projet implémente un scraper en Python pour extraire les informations des avocats à partir d'une page web. Le script extrait le nom, l'adresse, le numéro de téléphone et l'adresse e-mail de chaque avocat répertorié sur le site Web.

### AVERTISSEMENT

Ce projet est destiné à des fins éducatives et de recherche. Assurez-vous d'avoir l'autorisation de récupérer les données du site Web cible. Le scrapping non autorisé peut violer les conditions d'utilisation du site Web et peut être illégal dans certaines juridictions. Les auteurs déclinent toute responsabilité pour les actions réalisées avec ce code.

## Fonctionnalités

- **scraper.py** : Contient le code pour extraire les informations des avocats à partir du site web `https://www.barreaudenice.com/annuaire/avocats/`.
- **get_All_Page()** : Récupère toutes les pages de résultats de l'annuaire des avocats.
- **gratter_avocat()** : Scrappe les informations d'un avocat à partir d'une page.
- **grater_tous_les_avocats()** : Boucle sur toutes les pages et extrait les informations de tous les avocats.

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-utilisateur/projet-scrapping.git
cd projet-scrapping
```

Installez les dépendances nécessaires :
```bash
pip install requests beautifulsoup4
```
Utilisation
Exécutez le script pour extraire les informations des avocats :
```bash
python scraper.py
```
Le script va extraire les informations des avocats à partir du site web et les enregistrer dans un fichier avocats.txt situé dans le répertoire du projet.
Remarque

Assurez-vous d'avoir l'autorisation appropriée avant de scraper des données à partir d'un site Web.
Respectez les conditions d'utilisation du site Web cible pour éviter tout problème légal.
