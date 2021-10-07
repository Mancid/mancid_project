from flask import Blueprint, jsonify
from flask_login import login_required
from jinja2 import Template
from backend.database.db_mongo_tram import result_database, connect_db
from backend.database.db_refresh import HOST, PASSWORD, TRAM_SERVER

TRAM = Blueprint('tram', __name__)

@TRAM.route('/tram')
def parking():
    """This function return parkings in jinja2 in the front
    :returns: list of parkings in parking.html
    :rtype: jinja2
    """
    with open("./frontend/templates/tram.html") as file_:
        template = Template(file_.read())
        result = template.render()
    return result


@TRAM.route('/api/tram')
def views():
    return jsonify(result_database(connect_db(HOST, PASSWORD, TRAM_SERVER)))
