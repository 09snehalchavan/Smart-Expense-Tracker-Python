import sqlite3 as sql
from database import create_connection

create_connection()

def create_expense_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expense(
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            payment_mode TEXT NOT NULL,
            expense_date TEXT DEFAULT CURRENT_TIMESTAMP,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_expense_data(username, amount, category, payment_mode,description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expense (username, amount, category, payment_mode, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, amount, category, payment_mode, description))
    conn.commit()
    conn.close()


