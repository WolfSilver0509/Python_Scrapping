# Importation des librairies pandas request et beautifulsoup
import pandas as pd
import requests

from bs4 import BeautifulSoup as bs

# Listes mise dans la variables tous les livres
all_books = []

# Récupération de l'URL
#url = "https://books.toscrape.com/index.html"
def get_page(url): # fonction recupére la page
    # Telechargement de la page index
    page = requests.get(url)
    # création de l'objet Soup
    soup = bs(page.text, "lxml")
    return soup
    # A partir de là travaille d'inspection sur le sit index

def get_links(soup):
    # Récupération de tous les liens des livres
    links = []
    listings = soup.find_all(class_ ="product_pod")
    # A partir de chaques liens récupérer on peut obtenir le lien de livres
    for listing in listings:
        target_lnk = listing.find("h3").a.get("href")
        base_url = "https://books.toscrape.com/"
        complete_lnk = base_url + target_lnk
        #print(complete_lnk) # A partir de là nous avons tous les liens pour les livres répétorier sur la page actuelle
        links.append(complete_lnk)
    return links

def info_extract(links):
    #Extraire les informations de chaques liens
    for link in links:
        response = requests.get(link).text
        book_soup = bs(response,"lxml")

        title = book_soup.find(class_="col-sm-6 product_main").h1. text.strip()
        price = book_soup.find(class_="col-sm-6 product_main").p. text.strip()
        inStock = book_soup.find(class_="instock availability").text.strip()
        #img = book_soup.find(class_="item active").text.strip()

        #print(title, price, inStock) #Verification que tout fonctionne
        book = {"title":title,"price":price,"inStock":inStock}
        all_books.append(book)

url = "https://books.toscrape.com/index.html"
all_links = get_links(get_page(url))
info_extract(all_links)

print(len(all_books))
