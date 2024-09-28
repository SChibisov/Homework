import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

for i in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'Продукт{i}', f'Описание{i}', f'Цена{i * 100}'))
    connection.commit()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


connection.commit()
connection.close()
