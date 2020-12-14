# A python code to capture  all smart tvs(names and prices) in jumia and write to a csv file
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.jumia.co.ke/smart-tvs-2282/'
page = requests.get(URL).text
soup = BeautifulSoup(page, 'html.parser')

articles = soup.find_all('article', class_='prd _fb col c-prd')
# print(len(articles)) = 40 articles

# Write to a csv file
filename = 'smart_tvs.csv'

file = open(filename, 'w', newline = '')

#headers = 'Product_name, Price\n'
file_writer = csv.writer(file)

file_writer.writerow(['Product_name', 'Product_price'])

   
for article in articles:
    information = article.find_all('div', class_='info')
    product_name = article.h3.text
    
    price = article.find_all('div', class_='prc')
    product_price = price[0].text
    
    print(product_name)
    print(product_price)
    print()
    
    file_writer.writerow([product_name, product_price])
    
file.close()
    
 
   