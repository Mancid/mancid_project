from flask import Blueprint, jsonify, render_template
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db
from backend.function_velo.verdict import verdict, favorite
from backend.variable import AUTH_DB, HOST, PASSWORD, VELO_DB

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
    connexion = connect_db(HOST, PASSWORD, VELO_DB, "velo")
    return jsonify(result_db(connexion))


@VELO.route('/verdict')
def verdict_funct():
    location, velo, pos = favorite(HOST, PASSWORD,
                                   VELO_DB, "velo",
                                   AUTH_DB, "authentication"
                                   )
    verd = verdict()
    return render_template('verdict.html', location=location,
                           velo=velo, pos=pos, verd=verd
                           )
