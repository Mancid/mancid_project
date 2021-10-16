from flask import Blueprint, jsonify, render_template
from backend.database.db_connect import connect_db
from backend.database.db_mongo_tram import result_db
from backend.variable import HOST, PASSWORD, TRAM_SERVER

TRAM = Blueprint("tram", __name__)


@TRAM.route("/tram")
def tram():
    """This function return parkings in jinja2 in the front
    :returns: list of parkings in parking.html
    :rtype: jinja2
    """
    return render_template("tram.html")


@TRAM.route("/api/tram")
def views():
    connexion = connect_db(HOST, PASSWORD, TRAM_SERVER, "tram")
    return jsonify(result_db(connexion))
