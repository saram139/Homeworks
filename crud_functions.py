import sqlite3


def initiate_db():
    conn = sqlite3.connect("not_telegram2.db")
    cursor = conn.cursor()

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT,
                   price INTEGER NOT NULL
                   )
                   """
    )

    cursor.execute(
        "INSERT INTO Products (title, description, price) VALUES ('Че-нибудь', 'Описание 1', '100')"
    )
    cursor.execute(
        "INSERT INTO Products (title, description, price) VALUES ('Пофигин', 'Описание 2', '200')"
    )
    cursor.execute(
        "INSERT INTO Products (title, description, price) VALUES ('Смехозан', 'Описание 3', '300')"
    )
    cursor.execute(
        "INSERT INTO Products (title, description, price) VALUES ('Счастье', 'Описание 4', '400')"
    )

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("not_telegram2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    prod = cursor.fetchall()
    conn.commit()
    conn.close()
    return prod
