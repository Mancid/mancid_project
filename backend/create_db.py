from backend.create_dict_url import *
import sqlite3
import logging


def create_table():
    """This function create a table parking IF
    not exist, with 5 columns : Nom, Total, Free
    Heure and Status
    Nom is all of name of park in the function dict_url
    check the function dict_url for more information
    """
    create = """CREATE TABLE IF NOT EXISTS "Parking" (
    "Nom"    TEXT ,
    "Total"    TEXT,
    "Free"    TEXT,
    "Heure"    TEXT,
    "Status"TEXT
    );"""
    logging.debug('create the sql request')
    c.execute(create)
    for parking in dict_url().keys():
        name_park = """INSERT INTO Parking (Nom) VALUES (?)"""
        c.execute(name_park, (parking,))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    create_table()
    conn.commit()
