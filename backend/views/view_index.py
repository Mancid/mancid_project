from flask import render_template

route = '/'


def view():
    return render_template('index.html')
