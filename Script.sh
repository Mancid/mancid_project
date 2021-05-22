export SERVER_MONGO_DB="mancid.eoyjw.mongodb.net/"
export PASSWORD_MONGO_DB="iMn56LMeKIYdnmgU"
export HOST_MONGO_DB="dbMancid"
export FLASK_APP=backend
flask initdb
export FLASK_APP="backend/main:create_app('dev')"
flask run