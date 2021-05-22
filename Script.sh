export FLASK_APP=backend
flask initdb
export FLASK_APP="backend/main:create_app('dev')"
flask run
