import sqlite3 as sql

from database import create_connection

create_connection()

def create_income_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income(
            income_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            amount REAL NOT NULL,
            source TEXT NOT NULL,
            payment_mode TEXT NOT NULL,
            income_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_income_data(username,amount,source, payment_mode, income_date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO income (username, amount, source, payment_mode, income_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, amount, source, payment_mode, income_date))

    conn.commit()
    conn.close()
