from backend.function.dict_url import dict_url
from .connect_db import connect
import logging


def create_table(db):
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
    conn, c = connect(db)
    c.execute(create)
    for parking in dict_url().keys():
        name_park = """INSERT INTO Parking (Nom) VALUES (?)"""
        c.execute(name_park, (parking,))
    conn.commit()
    conn.close()
