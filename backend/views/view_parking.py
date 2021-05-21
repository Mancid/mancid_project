from backend.database.db_mongo import result_database

ROUTE = '/api/parking'


def view():
  """
  Returns page parking.html in json
  """
  return result_database('test.Parking')
