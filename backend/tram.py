from flask import Blueprint, jsonify
from flask_login import login_required
from jinja2 import Template
from backend.function_tram.dict_tram import dict_tram

TRAM = Blueprint('tram', __name__)

@TRAM.route('/tram')
# @login_required
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
# @login_required
def views():
    return jsonify(dict_tram())
