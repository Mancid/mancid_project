# main.py

from datetime import datetime
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from jinja2 import Template
from apscheduler.schedulers.background import BackgroundScheduler
from backend.database.db_mongo import result_database, connect_db, main_db
from backend.database.db_mongo import HOST, PASSWORD, SERVER


MAIN = Blueprint('main', __name__)



@MAIN.route('/')
def index():
  """Returns page index.html"""
  return render_template('index.html')


@MAIN.route('/profile')
@login_required
def profile():
  """Returns page profile.html with name and email of the user"""
  return render_template('profile.html', name=current_user.name,
                         mail=current_user.email)


@MAIN.route('/parking')
@login_required
def parking():
  """
  This function return parkings in jinja2 in the front
  """
  parkings = result_database(connect_db(HOST, PASSWORD, SERVER))
  now = datetime.now().strftime("%H:%M")
  with open("front/parking.html") as file_:
    template = Template(file_.read())
    result = template.render(parkings=parkings, now=now)
  return result


# SCHED = BackgroundScheduler(daemon=True)
# SCHED.add_job(main_db, 'interval', seconds=59)
# SCHED.start()
# main_db()
