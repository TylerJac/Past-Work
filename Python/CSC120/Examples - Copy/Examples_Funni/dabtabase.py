import sqlite3


def init_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Products")

    cursor.execute("""CREATE TABLE Products(ProductID INTEGER PRIMARY KEY NOT NULL,"
                   Description TEXT,
                   UnitCost REAL,
                   RetailPrice REAL,
                   UnitOnHand INTEGER)""")


def add_pro(cursor):
    cursor.execute(""" INSERT INFO Products(ProductID INTEGER PRIMARY KEY NOT NULL,"
                   Description,
                   UnitCost,
                   RetailPrice,
                   UnitOnHand)
                   # VALUES(1, "Dark Chocolate Bar", 2.99, 5.99, 197)
                   #      (2, "Medium Dark Chocolate Bar", 2.99, 5.99, 406)
                   # (3, "Milk Chocolate Bar", 2.99, 5.99, 266)
                   # (4, "Chocolate Truffles", 2.99, 5.99, 398)
                   # (5, "Chocolate Caramel Bar", 2.99, 5.99, 272)
                   # (6, "Chocolate Raspberry Bar", 2.99, 5.99, 363)
                   # (7, "Chocolate and Cashew Bar", 2.99, 5.99, 325)
                   # (8, "Hot Chocolate Mix", 2.99, 5.99, 222)
                   # (9, "semisweet Chocolate Chips", 2.99, 5.99, 163)
                   # (10, "white Chocolate chips", 2.99, 5.99, 293""")

    products = [(1, "Dark Chocolate Bar", 2.99, 5.99, 197),
                (2, "Medium Dark Chocolate Bar", 2.99, 5.99, 406),
                (3, "Milk Chocolate Bar", 2.99, 5.99, 266),
                (4, "Chocolate Truffles", 2.99, 5.99, 398),
                (5, "Chocolate Caramel Bar", 2.99, 5.99, 272),
                (6, "Chocolate Raspberry Bar", 2.99, 5.99, 363),
                (7, "Chocolate and Cashew Bar", 2.99, 5.99, 325),
                (8, "Hot Chocolate Mix", 2.99, 5.99, 222),
                (9, "semisweet Chocolate Chips", 2.99, 5.99, 163),
                (10, "white Chocolate chips", 2.99, 5.99, 293)]

    for p in products:
        cursor.execute("""INSERT INFO Products(Description, UnitCost, RetailPrice, UnitOnHand)
        VALUES (?, ?, ?, ?, ?)""", (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10]))


def display_pro(cursor):
    print("")
    cursor.execute("SELECT* FROM Products")
    products = cursor.fetchall()
    print(f"{'ProductID' :<16}{'Description':30}{'UnitCost' :<16}{'RetailPrice' :<16}{'UnitOnHand'}")
    for product in products:
        print(f"{product[0]:<16} {product[1]:30} {product[2]:<16} {product[3]:<16} {product[4]}")


def main():
    connection = sqlite3.connect("dabtabase.db")
    cursor = connection.cursor()
    init_table(cursor)
    add_pro(cursor)

    connection.commit()
    display_pro(cursor)

    connection.close()
