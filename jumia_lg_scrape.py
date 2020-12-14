import csv
import requests
from bs4 import BeautifulSoup

# Scraping Jumia web for all Lg brand products

URL = 'https://www.jumia.co.ke/mlp-lg-store/'
page = requests.get(URL).text
soup = BeautifulSoup(page, 'html.parser')

articles = soup.find_all('article', class_='prd _fb col c-prd')
# print(len(articles))

filename = 'lg_brand_products.csv'

file = open(filename, 'w', newline= '')

file_writer = csv.writer(file)

file_writer.writerow(['Product name', 'Product price'])

for article in articles:
    product_name = article.h3.text
    
    price = article.find_all('div', class_='prc')
    product_price = price[0].text
    
    print(product_name)
    print(product_price)
    print()
    
    file_writer.writerow([product_name, product_price])
    
file.close()
