# main.py

from jinja2 import Template
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from backend.database.db_mongo import result_database, connect_db, main_db
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
  return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name,
                          mail=current_user.email)


@main.route('/parking')
@login_required
def parking():
  """
  This function return parkings in jinja2 in the front
  """
  parkings = result_database(connect_db())
  now = datetime.now().strftime("%H:%M")
  with open("front/parking.html") as file_:
    template = Template(file_.read())
    result = template.render(parkings=parkings, now=now)
  return result


sched = BackgroundScheduler(daemon=True)
sched.add_job(main_db, 'interval', seconds=59)
sched.start()
main_db()
