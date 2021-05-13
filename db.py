import sqlite3

conn = sqlite3.connect('end.db')
c = conn.cursor()


c.execute('''CREATE TABLE product(category TEXT, subcategory TEXT, title TEXXT,subtitle TEXT,product TXET,price INT)''')



category ='периферия'
subcategory = 'геймърски-мишки'
title = 'Spartan Gear Talos'
subtitle  = 'Геймърска мишка Spartan Gear Talos, черен'
product number = 'SG-033885'
price = '15.00'



c.execute('''INSERT INTO product VALUES(?,?,?,?,?,?,?)''', (category,subcategory,title,subtitle,product,price )
conn.commit()


c.execute('''SELECT * FROM products''')
results = c.fetchall()
print(results)


conn.close()
