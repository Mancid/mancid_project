from flask import render_template

ROUTE = '/'


def view():
  """Returns page index.html"""
  return render_template('index.html')
