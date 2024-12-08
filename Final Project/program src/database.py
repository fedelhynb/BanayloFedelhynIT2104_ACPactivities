import sqlite3

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect('rental_system.db')
        self.cursor = self.conn.cursor()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def close(self):
        self.conn.close()
