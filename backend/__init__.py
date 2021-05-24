import os
from flask import Flask
from flask_login import LoginManager
from backend.models import DB
from backend.models import User
from .auth import AUTH as auth_blueprint
from .main import MAIN as main_blueprint


def create_app():
  """
  This function is the flask run
  """
  app = Flask(__name__)

  DB.create_all()

  # app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
  app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    # since the user_id is just the primary key of our user table,
    # use it in the query for the user
    return DB.query(User).get(int(user_id))

  # blueprint for auth routes in our app
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  app.register_blueprint(main_blueprint)

  # app.run(debug=True)

  return app
