from flask import Blueprint, render_template, session, redirect, url_for


MAIN = Blueprint("main", __name__)


@MAIN.route("/")
def index():
    """Returns page login.html
    :returns: page login.html
    :rtype: html
    """
    return render_template("index.html")


@MAIN.route("/profile")
def profile():
    """Returns page profile.html with name and email of the user
    :returns: page profile.html
    :rtype: html
    """
    if "email" in session:
        email = session["email"]
        return render_template("profile.html", email=email)

    return redirect(url_for("auth.login"))
