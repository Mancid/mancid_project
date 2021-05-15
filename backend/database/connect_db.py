import sqlite3


def connect(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return conn, c
