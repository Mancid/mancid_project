from flask import Blueprint, jsonify, render_template
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db
from backend.variable import HOST, PASSWORD, TRAM_SERVER

VELO = Blueprint("velo", __name__)


@VELO.route("/velo")
def velo():
    """This function return the front velomagg
    :returns: front of velomagg.html
    :rtype: html
    """
    return render_template("velo.html")


@VELO.route("/api/velo")
def views():
    """This function return the api velomagg
    :returns: list of velomagg in api
    :rtype: json
    """
    connexion = connect_db(HOST, PASSWORD, TRAM_SERVER, "tram")
    return jsonify(result_db(connexion))
