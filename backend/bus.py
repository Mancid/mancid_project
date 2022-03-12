from operator import itemgetter
from flask import Blueprint, jsonify, render_template
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db
from backend.variable import HOST, PASSWORD, BUS_DB

BUS = Blueprint("bus", __name__)


@BUS.route("/bus")
def bus():
    """This function return the front bus
    :returns: front of bus.html
    :rtype: html
    """
    return render_template("bus.html")


@BUS.route("/api/bus")
def views():
    """This function return the api bus
    :returns: list of bus in api
    :rtype: json
    """
    connexion = connect_db(HOST, PASSWORD, BUS_DB, "bus")
    result_sorted = sorted(result_db(connexion), key=itemgetter("Delai"))
    return jsonify(result_sorted)
