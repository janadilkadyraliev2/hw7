from db import create_connection


def add_products():
    """Добавление товаров в базу данных."""
    products = [
        ('Товар 1', 10.99, 20),
        ('Товар 2', 15.49, 30),
        ('Товар 3', 5.00, 50),
        ('Товар 4', 25.00, 10),
        ('Товар 5', 100.00, 5),
        ('Товар 6', 200.00, 8),
        ('Товар 7', 3.75, 100),
        ('Товар 8', 50.00, 15),
        ('Товар 9', 75.25, 2),
        ('Товар 10', 10.00, 12),
        ('Товар 11', 45.60, 7),
        ('Товар 12', 80.99, 0),
        ('Товар 13', 20.00, 3),
        ('Товар 14', 60.00, 1),
        ('Товар 15', 30.00, 9),
    ]

    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
    ''', products)
    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    """Изменение количества товара по id."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    """Изменение цены товара по id."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    """Удаление товара по id."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()
    conn.close()


def fetch_all_products():
    """Выбор всех товаров и их вывод в консоль."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    for product in products:
        print(product)


def fetch_products_by_price_and_quantity(max_price, min_quantity):
    """Поиск товаров по цене и количеству."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products WHERE price < ? AND quantity > ?
    ''', (max_price, min_quantity))
    products = cursor.fetchall()
    conn.close()

    for product in products:
        print(product)


def search_products_by_title(keyword):
    """Поиск товаров по названию."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    products = cursor.fetchall()
    conn.close()

    for product in products:
        print(product)
