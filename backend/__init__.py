from flask import Flask
from .database.create_db import create_table
from .database.update_db import update_table
app = Flask(__name__)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    create_table('Parking.db')
    update_table('Parking.db')
    print('Initialized the database.')
