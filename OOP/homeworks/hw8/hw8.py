import sqlite3


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)


products = [
        ("Мыло Детское", 90, 100),
        ("Стиральный Порошок TIDE 4.5кг", 450, 190),
        ("Печение Олег", 240, 1900),
        ("Стиральная Машина Леха", 12350, 15),
        ("Ноутбук ASUS fre0", 45000, 10),
        ("Хз что", 40, 20),
        ("Симкарта Beeline", 20, 100),
        ("Симкарта Megacom", 20, 100),
        ("Симкарта O!", 20, 150),
        ("Подгузники GGIIG 50шт", 450, 290),
        ("Печение Олег", 380, 290),
        ("Игровая мышь Razor hd234", 4500, 30),
        ("Стиральный Порошок TIDE 4.5кг", 450, 190),
        ("Видеокарта NVIDIA RTX 5090", 209000, 20),
        ("Стиральный Порошок Ушастый нянь 4.5кг", 350, 10)
    ]
def create_products(conn,  product: tuple):
    sql = '''INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?);''' , products
    cursor = conn.cursor()
    cursor.execute(sql, product)
    conn.commit()


def update_product_quantity(conn, id:int, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_quantity, id,))
    conn.commit
    

def update_product_price(conn, id:int, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_price, id,))
    conn.commit()


def delete_product(conn, id:int):
    sql = '''DELETE FROM products WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()


def select_all_product(conn):
    sql = '''SELECT * FROM products;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)


def select_cheap(conn):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)


def search_product(conn, keyword):
    cursor = conn.cursor()
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    settings = ('%' + keyword + '%',)
    rows = cursor.execute(sql, settings).fetchall()
    
    print("Результаты поиска:")
    for row in rows:
        print(row)


sql_create_table = '''
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) DEFAULT 0.0 NOT NULL,
quantity INTEGER (5) DEFAULT 0 NOT NULL
);
'''

connection = create_connection("products.db")
if connection:
    print("База данных подключена")
    # create_table(connection, sql_create_table)
    # update_product_quantity(connection, 1 , 300)
    # update_product_price(connection, 7, 60)
    # delete_product(connection, 11)
    # select_all_product(connection)
    # select_cheap(connection)
    search_product(connection, "П")

