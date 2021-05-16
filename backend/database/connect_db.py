import sqlite3


def connect(database):
  """
  this function allows to connect to the database 'database'.
  conn represents the connection to the database
  cursor allows to place a cursor in the database
  """
  conn = sqlite3.connect(database)
  cursor = conn.cursor()
  return conn, cursor
