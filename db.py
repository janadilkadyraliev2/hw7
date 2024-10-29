import sqlite3

def create_connection(db_file):
    """Создание подключения к базе данных SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

def create_database():
    """Создание базы данных и таблицы."""
    conn = create_connection('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
