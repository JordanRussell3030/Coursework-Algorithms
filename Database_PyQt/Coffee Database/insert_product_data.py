import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql, values)
        db.commit()

if __name__ == "__main__":
    product = ("Espresso", 1.5)
    insert_data(product)
    product_2 = ("Latte", 1.35)
    insert_data(product_2)
    product_3 = ("Mocha", 2.4)
    insert_data(product_3)
    product_4 = ("Green Tea", 1.2)
    insert_data(product_4)
    product_5 = ("Black Tea", 1)
    insert_data(product_5)
    product_6 = ("Americano", 1.5)
    insert_data(product_6)
