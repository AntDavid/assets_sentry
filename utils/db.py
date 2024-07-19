import _sqlite3
import streamlit as st

def create_connection(db_file):
    conn = None

    try:
        conn = _sqlite3.connect(db_file)

    except _sqlite3.Error as e:
        st.error(e)

    return conn

def creat_table(conn):
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(create_users_table)
    
    except _sqlite3.Error as e:
        st.error(e)
    
def add_user(conn, name, email, username, password):
    add_user = """
    INSERT INTO users (name, email, username, password)
    VALUES (?, ?, ?, ?);
    """

    try:
        cursor = conn.cursor()
        cursor.execute(add_user, (name, email, username, password))
        conn.commit()
    
    except _sqlite3.Error as e:
        st.error(e)
    
    return cursor.lastrowid

def verify_user(conn, username, password):
    sql = '''SELECT * FROM users WHERE username = ? AND password = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    user = cursor.fetchone()
    return user
