How to save scraped data to a database

import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

#create connection
conn = sqlite3.connect('cputest.db')
c = conn.cursor()

#scraping function and insert
def getPriceOVC(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    store = 'OVC'
    title = soup.find('h1').text.strip().replace('\n','')
    price = soup.find('div', {'class': 'article_details_price'}).text.replace('*', '').strip().replace('£', '')
    stock = soup.find('span', {'class': 'popup-text'}).text.strip()
    c.execute('''INSERT INTO prices VALUES(?,?,?,?,?,?)''',(category,subcategory,title,subtitle,product,price))
    
    return



getPriceOVC('https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D0%BF%D0%B5%D1%80%D0%B8%D1%84%D0%B5%D1%80%D0%B8%D1%8F')
conn.commit()
print('complete.')

#select all from table
c.execute('''SELECT * FROM prices''')
results = c.fetchall()
print(results)

#close connection
conn.close()
