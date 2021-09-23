from datetime import datetime
from flask import Blueprint
from flask_login import login_required
from jinja2 import Template
from backend.database.db_mongo_park import result_database, connect_db
from backend.database.db_mongo_park import HOST, PASSWORD, PARKING_SERVER

PARKING = Blueprint('parking', __name__)


@PARKING.route('/parking')
# @login_required
def parking():
  """This function return parkings in jinja2 in the front
  :returns: list of parkings in parking.html
  :rtype: jinja2
  """
  parkings = result_database(connect_db(HOST, PASSWORD, PARKING_SERVER))
  now = datetime.now().strftime("%H:%M")
  with open("./frontend/templates/parking.html") as file_:
    template = Template(file_.read())
    result = template.render(parkings=parkings, now=now)
  return result