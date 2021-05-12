from flask import jsonify
from .function_db import all_infos

route = '/api/parking'


def view():
    parking, nom = all_infos()
    return jsonify(parking, nom)
