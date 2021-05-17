from backend.database.db_mongo import main

ROUTE = '/api/parking'


def view():
  """
  Returns page parking.html in json
  """
  return main()
