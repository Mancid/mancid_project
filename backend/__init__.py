import os
from backend.database import db_refresh
from flask import Flask
from flask_cors import CORS
# from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler
from .auth import AUTH as auth_blueprint
from .main import MAIN as main_blueprint
from .parking import PARKING as parking_blueprint
from .tram import TRAM as tram_blueprint


def create_app(config_name):
    """This function is for the flask run we initialize
    all configuration like templates folder and static
    folder for the front-end, the DB and the neccesary for
    login.

    :returns: Flask app
    :rtype: Flask
    """
    db_refresh.refresh()
    SCHED = BackgroundScheduler(daemon=True)
    SCHED.start()
    SCHED.add_job(db_refresh.refresh, 'interval', seconds=120)

    app = Flask(__name__,
                template_folder='../frontend/templates/',
                static_folder='../frontend/static')

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     # since the user_id is just the primary key of our user table,
    #     # use it in the query for the user
    #     return DB.query(User).get(int(user_id))

    # blueprint for auth routes in our app
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    app.register_blueprint(main_blueprint)

    # blueprint for non-auth parts of app
    app.register_blueprint(parking_blueprint)

    # blueprint for non-auth parts of app
    app.register_blueprint(tram_blueprint)

    # app.run(debug=True)
    return app
