import os
import logging
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig(
format='%(asctime)s %(message)s',
level=logging.DEBUG)

sched = BackgroundScheduler(daemon=True)
sched.add_job(main,'interval',seconds=59)
sched.start()

template_dir = os.path.abspath('./front/templates')
app = Flask(__name__, template_folder=template_dir)

CORS(app)

