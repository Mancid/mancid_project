import logging
import sqlite3
from .connect_db import connect


def function_table(database):
  """
  This function return all row
  in the database, with table name Parking
  """
  res = []
  conn, cursor = connect(database)
  logging.info("connect to db with cursor %s", cursor)
  cursor.row_factory = sqlite3.Row
  logging.info("initializing the cursor for return dict")
  cursor.execute("SELECT * FROM Parking")
  logging.debug("select all rows in database")
  for row in cursor.fetchall():
    res.append(dict(row))
    # for i in res:
    #   title = (i.get('Nom'))
    #   if title not in nom:
    #     nom.append(title)
  conn.commit()
  conn.close()
  logging.info("this is the row in the database %s", res)
  return res  #, nom
