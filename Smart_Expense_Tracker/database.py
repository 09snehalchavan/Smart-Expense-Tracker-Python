import sqlite3 as sql

# create a function to create a database connection

def create_connection():
    
    conn = sql.connect('database.db')
    return conn

# Create a function to create a table
def create_table():
    
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone_number TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()
    
def register_user(name, username, password, phone_number):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (name, username, password, phone_number)
        VALUES (?, ?, ?, ?)
    ''', (name, username, password, phone_number))
    
    conn.commit()
    conn.close()

def check_user_exists(username):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE username = (?)
    ''', (username,))

    user = cursor.fetchone()
    conn.close()

    return user 

def check_user_login(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
                   ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_password(username, new_password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users SET password = ? WHERE username = ?
    ''', (new_password, username))

    conn.commit()
    conn.close()