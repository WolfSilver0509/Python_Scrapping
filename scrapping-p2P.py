import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/index.html"
page = requests.get(url)
# Voir le code html source
soup = BeautifulSoup(page.content, 'html.parser')
#cat = soup.find_all("div", class_="side_categories")
#cat = soup.find("div", { "class" : "side_categories" }).findAll("a", recursive=False)
#categories = cat.findChildren("a")
#for div in cat:

#div = soup.find("div", { "class" : "side_categories" })
#cat = div.find_all("a") # returns a list of all <li> children of li

#ul = soup.find("ul", {"class":"nav nav-list"})
#cat = ul.find_all("ul")
print(soup)