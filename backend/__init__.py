import os
import importlib
from flask import Flask


def create_app(config_name):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    views = []
    current_directory = os.path.dirname(os.path.realpath(__file__))

    for filename in os.listdir(current_directory + '/views'):
        if filename.endswith(".py") and filename.startswith("view_"):
            views.append(filename[5:-3])

    for view in views:
        mod = importlib.import_module(f'backend.views.view_{view}')
        if getattr(mod, 'disabled', None):
            continue
        print(f'[*]Loading view {view} with route {mod.route}')
        app.add_url_rule(mod.route, view, view_func=mod.view)

    return app
