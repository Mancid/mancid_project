from flask import render_template

ROUTE = '/parking'


def view():
  """Returns page parking.html"""
  return render_template('parking.html')
