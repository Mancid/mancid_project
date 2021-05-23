from flask import Flask
from backend.database.db_mongo import main
APP = Flask(__name__)


@APP.cli.command("initdb")
def initdb_command():
  """Initializes the database."""
  print("Start of database initialization")
  main()
  print("The initialization of the database is completed")
