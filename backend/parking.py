from backend.database.db_connect import connect_db
from backend.database.db_mongo_park import result_db
from flask import Blueprint, jsonify, render_template
from backend.database.db_refresh import HOST, PASSWORD, PARKING_SERVER

PARKING = Blueprint('parking', __name__)


@PARKING.route('/parking')
def parking():
    """This function return parkings in jinja2 in the front
    :returns: list of parkings in parking.html
    :rtype: jinja2
    """
    return render_template('parking.html')


@PARKING.route('/api/parking')
def views():
    connexion = connect_db(HOST, PASSWORD, PARKING_SERVER, "parking")
    return jsonify(result_db(connexion))
