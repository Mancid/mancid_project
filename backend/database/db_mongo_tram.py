#pylint: disable=E0401
import logging
import os
from pymongo import MongoClient
from backend.function_tram.dict_tram import dict_tram

HOST = os.environ["HOST_MONGO_DB"]
PASSWORD = os.environ["PASSWORD_MONGO_DB"]
TRAM_SERVER = os.environ["TRAM_SERVER"]


def connect_db(host, password, tram_server):
  """ This function connect in atlas a mongodb

  :returns: connection to atlas mongo db
  :rtype: connection string
  """
  client = MongoClient(f"mongodb+srv://{host}:{password}@{tram_server}?ssl=true&"\
                       "ssl_cert_reqs=CERT_NONE")
  logging.info(" %s client : ", client)
  conn = client.test
  logging.info(" your database : %s", conn)
  database = conn["Tram"]
  return database


def insert_rows(database):
  """This function insert rows in the database
  mongodatabase
  
  :returns: inserts rows in the database
  :rtype: rows in database
  """
  values = dict_tram()
  logging.info("%s this is the values add in database", values)
  return database.insert(values)


def remove(database):
  """ This function remove all rows in database mongodatabase

  :returns: Remove all rows in database
  :rtype: remove
  """
  logging.info("remove all rows in database mongodatabase")
  return database.remove({})


def result_database(database, station):
  """ This function return the result with all
  name in parking. They return a dict

  :returns: a dict with all rows in database
  :rtype: dict
  """
  res = []
  myquery = {"Arrêt": station}
  for rows in database.find(myquery):
    logging.info("this is all rows in database :  %s", rows)
    res.append(rows)
  logging.info("this is your dict with the value in db %s", res)
  return res


def main_db():
  """This is the main function to call
  all other functions

  :returns: connection, remove, insert and result
  :rtype: main function
  """
  my_db = connect_db(HOST, PASSWORD, TRAM_SERVER)
  remove(my_db)
  insert_rows(my_db)
