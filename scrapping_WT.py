import requests
from bs4 import BeautifulSoup
import csv

#MAIN

pages = ["http://winetime.com.ua/white-wine/"]
pas = 0
for x in range(16):
    pas+=30
    page = "http://winetime.com.ua/white-wine/page/{}.htm?type_tovar=publish&amp;size=30".format(pas)
    pages.append(page)

file_name = input("File name: ") + '.csv'
f = csv.writer(open(file_name, 'w'), delimiter=";")

counter = 0
for item in pages:
    counter += 1
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    wine_list = soup.find(class_='col-xs-10 catalog_right katalog_tovars footer-100')
    
    needless1 = soup.find(class_='top_cat')
    needless1.decompose()
    needless2 = soup.find(class_='catalog_blocks-nav')
    needless2.decompose()
    needless3 = soup.find(class_='text-center')
    needless3.decompose()
    
    names = wine_list.find_all(class_='mainlink')
    prices = wine_list.find_all(class_='main_price')
    
    for x in range(len(names)):
        name = names[x].get_text()
        price = prices[x]['price']
        f.writerow([name, price])
    print(counter, 'Page DONE')
    