import logging
from pymongo import MongoClient
from backend.function.parse_xml import create_dict
from backend.function.dict_url import dict_url


def create_database():
  """ This function connect in localhost a mongodb
  """
  client = MongoClient(host="localhost", port=27017)
  logging.info(" %s client : ", client)
  conn = client["database"]
  logging.info(" your database : %s", conn)
  database = conn['Parking']
  return database


def insert_rows(database):
  """This function insert rows in the database
  mongodatabase
  database : is the database want to be inserted
  """
  values = create_dict(dict_url())
  logging.info("%s this is the values add in database", values)
  return database.insert(values)



def remove(database):
  """ This function remove all rows in database mongodatabase
  """
  logging.info("remove all rows in database mongodatabase")
  return database.remove({})


def result_database(database):
  """ This function return the result with all
  name in parking. They return a dict
  """
  res = {}
  for i in dict_url():
    for rows in database.find({}, {i}):
      logging.info("this is all rows in database :  %s", rows)
      parking = i
      res[parking] = rows.get(i)
  logging.info("this is your dict with the value in db %s", res)
  return dict(sorted(res.items()))



def parse_dict(mydict):
  for parking, value in mydict.items():
    logging.info("this is your dict %s, %s",parking, value)
    print(parking,value)


def main():
  """
  This is the main function to call
  all other functions
  """

  my_db = create_database()
  remove(my_db)
  insert_rows(my_db)
  my_dict = result_database(my_db)
  parse_dict(my_dict)


if __name__ == '__main__':
  main()
