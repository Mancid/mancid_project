export FLASK_APP="backend"
# gunicorn --bind 0.0.0.0:5000 wsgi:app
gunicorn --bind 0.0.0.0:${PORT} wsgi:app
