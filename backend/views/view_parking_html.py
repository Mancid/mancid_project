from flask import render_template

route = '/parking'
disabled = False


def view():
    return render_template('parking.html')
