import sqlite3

class Database:
    @staticmethod
    def connect():
        return sqlite3.connect('dine_in_solution.db')

    @staticmethod
    def create_tables():
        with Database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    location TEXT,
                    cuisine_type TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    restaurant_id INTEGER,
                    customer_name TEXT,
                    items TEXT,
                    total_price REAL,
                    status TEXT,
                    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
                )
            ''')

    @staticmethod
    def insert(table, data):
        with Database.connect() as conn:
            cursor = conn.cursor()
            columns = ', '.join(data.keys())
            placeholders = ', '.join('?' for _ in data)
            cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({placeholders})', tuple(data.values()))
            return cursor.lastrowid

    @staticmethod
    def update(table, record_id, data):
        with Database.connect() as conn:
            cursor = conn.cursor()
            columns = ', '.join(f'{key} = ?' for key in data)
            cursor.execute(f'UPDATE {table} SET {columns} WHERE id = ?', (*data.values(), record_id))

    @staticmethod
    def delete(table, record_id):
        with Database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table} WHERE id = ?', (record_id,))

    @staticmethod
    def select_all(table):
        with Database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table}')
            return cursor.fetchall()

    @staticmethod
    def select_one(table, record_id):
        with Database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table} WHERE id = ?', (record_id,))
            return cursor.fetchone()

    @staticmethod
    def select_where(table, column, value):
        with Database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table} WHERE {column} = ?', (value,))
            return cursor.fetchall()
