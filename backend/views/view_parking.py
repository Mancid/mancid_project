from flask import jsonify
from backend.database.function_db import function_table

route = '/api/parking'


def view():
    parking, nom = function_table('parking.db')
    return jsonify(parking, nom)
