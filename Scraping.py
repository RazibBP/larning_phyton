import requests as rq
from bs4 import BeautifulSoup as bs



url = "https://www.othoba.com/laptop?orderby=5&pagesize=1"
html = rq.get(url)
shop = bs(html.text, "html.parser")

list = sh.findAll("div",{"class":"dl-all-product-from-pages"})
list = shp.findAll("div",{"class":"dl-all-product-from-pages"})
list = shop.findAll("div",{"class":"dl-all-product-from-pages"})
list = shop.findAll("div",{"class":"dl-all-product-from-pages"})
amount = shop.findAll("dev",{"class":"product-price"})
amount = shop.findAll("dev",{"class":"product-price"})
print(amount)
#print(len(list))

title =[]
price = []

for x in list:
    title.append(x.h4.a.text)
print(title)

for x in amount:
    price.append(x.sstext)
print(price)

