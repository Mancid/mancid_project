from flask import Flask
from backend.database.create_db import create_table
from backend.database.update_db import update_table
APP = Flask(__name__)


@APP.cli.command('initdb')
def initdb_command():
  """Initializes the database."""
  create_table('Parking.db')
  update_table('Parking.db')
  print('Initialized the database.')
