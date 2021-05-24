import os
from sqla_wrapper import SQLAlchemy
from flask_login import UserMixin

DB = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite://db.sqlite"))
# this connects to a database either on Heroku or on localhost


class User(UserMixin, DB.Model):
  """
  This class create a model for a user with Column id, email, password and name
  """
  # primary keys are required by SQLAlchemy
  id = DB.Column(DB.Integer, primary_key=True)
  email = DB.Column(DB.String(100), unique=True)
  password = DB.Column(DB.String(100))
  name = DB.Column(DB.String(1000))
