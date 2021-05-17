import logging
from backend.function.dict_url import dict_url
from .connect_db import connect


def create_table(database):
  """
  This function create a table parking IF
  not exist, with 5 columns : Nom, Total, Free
  Heure and Status
  Nom is all of name of park in the function dict_url
  check the function dict_url for more information
  """
  logging.debug('create the sql request')
  conn, cursor = connect(database)
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS "Parking" (
  "Nom"    TEXT ,
  "Total"    TEXT,
  "Free"    TEXT,
  "Heure"    TEXT,
  "Status"TEXT
  );""")
  for parking in dict_url():
    cursor.execute("""INSERT INTO Parking (Nom) VALUES (?)""", (parking,))
  conn.commit()
  conn.close()
