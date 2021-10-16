from flask import Blueprint, jsonify, render_template
from backend.database.db_connect import connect_db
from backend.database.db_mongo_tram import result_db
from backend.variable import HOST, PASSWORD, TRAM_SERVER

VELO = Blueprint("velo", __name__)


@VELO.route("/velo")
def velo():
    """This function return parkings in jinja2 in the front
    :returns: list of parkings in parking.html
    :rtype: jinja2
    """
    return render_template("velo.html")


@VELO.route("/api/velo")
def views():
    connexion = connect_db(HOST, PASSWORD, TRAM_SERVER, "tram")
    return jsonify(result_db(connexion))
