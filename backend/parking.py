from flask import Blueprint, jsonify, render_template
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db
from backend.variable import HOST, PASSWORD, PARKING_SERVER

PARKING = Blueprint("parking", __name__)


@PARKING.route("/parking")
def parking():
    """This function return the front parking
    :returns: front of parking.html
    :rtype: html
    """
    return render_template("parking.html")


@PARKING.route("/api/parking")
def views():
    """This function return the api parking
    :returns: list of parking in api
    :rtype: json
    """
    connexion = connect_db(HOST, PASSWORD, PARKING_SERVER, "parking")
    return jsonify(result_db(connexion))
