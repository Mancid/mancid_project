import os
import psycopg2
from sqla_wrapper import SQLAlchemy
from flask_login import UserMixin

url = os.environ["DATABASE_SQL"]
# DB = psycopg2.connect(f"postgresql://{url}", sslmode='require')
DB = SQLAlchemy(f"postgresql://{url}")
# DB = SQLAlchemy("sqlite:///db.sqlite")
# this connects to a database either on Heroku or on localhost


class User(UserMixin, DB.Model):
  """This class create a model for a user with Column id, email
  password and name

  :returns: Database models for Users
  :rtype: Database SQLAlchemy
  """
  # primary keys are required by SQLAlchemy
  id = DB.Column(DB.Integer, primary_key=True)
  email = DB.Column(DB.String(100), unique=True)
  password = DB.Column(DB.String(100))
  name = DB.Column(DB.String(1000))
