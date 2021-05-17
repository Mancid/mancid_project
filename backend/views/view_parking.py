from flask import jsonify
from backend.database.function_db import function_table

ROUTE = '/api/parking'


def view():
  """
  Returns page parking.html in json
  """
  parking = function_table('parking.db')
  return jsonify(parking)
