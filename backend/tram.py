from operator import itemgetter
from flask import Blueprint, jsonify, render_template
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db
from backend.variable import HOST, PASSWORD, TRAM_DB

TRAM = Blueprint("tram", __name__)


@TRAM.route("/tram")
def tram():
    """This function return the front tram
    :returns: front of tram.html
    :rtype: html
    """
    return render_template("tram.html")


@TRAM.route("/api/tram")
def views():
    """This function return the api tram
    :returns: list of tram in api
    :rtype: json
    """
    connexion = connect_db(HOST, PASSWORD, TRAM_DB, "tram")
    result_sorted = sorted(result_db(connexion), key=itemgetter("Delai"))
    return jsonify(result_sorted)
