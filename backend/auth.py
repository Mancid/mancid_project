import bcrypt
from flask import Blueprint, render_template, redirect, url_for, \
                  request, session
from backend.database.db_connect import connect_db
from backend.function_velo.all_favorite import all_favorite
from backend.variable import HOST, PASSWORD, VELO_DB, AUTH_DB


AUTH = Blueprint("auth", __name__)


@AUTH.route("/login", methods=["POST", "GET"])
def login():
    """This function return the form for login
    :returns: front login of login.html
    :rtype: html
    """
    records = connect_db(HOST, PASSWORD, AUTH_DB, "authentication")
    message = "Please login to your account"
    if "email" in session:
        return redirect(url_for("auth.logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found["email"]
            passwordcheck = email_found["password"]
            # encode the password and check if it matches
            if bcrypt.checkpw(password.encode("utf-8"), passwordcheck):
                session["email"] = email_val
                return redirect(url_for("auth.logged_in"))
            else:
                if "email" in session:
                    return redirect(url_for("auth.logged_in"))
                message = "Wrong password"
                return render_template("login.html", message=message)

        message = "Email not found"
        return render_template("login.html", message=message)

    return render_template("login.html", message=message)


@AUTH.route("/signin", methods=["post", "get"])
def signin():
    """This function return the form for signin
    :returns: front signin of signin.html
    :rtype: html
    """
    records = connect_db(HOST, PASSWORD, AUTH_DB, "authentication")
    message = ""
    # if method post in index
    if "email" in session:
        return redirect(url_for("auth.logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        favorite = request.form.get("favorite")
        # if found in database showcase that it"s found
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = "There already is a user by that name"
            return render_template("index.html", message=message)
        if email_found:
            message = "This email already exists in database"
            return render_template("index.html", message=message)
        if password1 != password2:
            message = "Passwords should match!"
            return render_template("index.html", message=message)
        if favorite == "":
            message = "Favorite not select ! Please select a favorite"
            return render_template("index.html", message=message)

        # hash the password and encode it
        hashed = bcrypt.hashpw(password2.encode("utf-8"), bcrypt.gensalt())
        # assing them in a dictionary in key value pairs
        user_input = {"name": user, "email": email,
                      "password": hashed, "favorite": favorite}
        # insert it in the record collection
        records.insert_one(user_input)

        # find the new created account and its email
        user_data = records.find_one({"email": email})
        new_email = user_data["email"]
        # if registered redirect to logged in as the registered user
        return render_template("logged_in.html", email=new_email)

    choice = all_favorite(HOST, PASSWORD, VELO_DB, "velo")
    return render_template("signin.html", choice=choice)


@AUTH.route("/logged_in")
def logged_in():
    """This function return the logged_in
    :returns: front logged_in of logged_in.html
    :rtype: html
    """
    if "email" in session:
        email = session["email"]
        return render_template("logged_in.html", email=email)

    return redirect(url_for("auth.login"))


@AUTH.route("/signout", methods=["POST", "GET"])
def logout():
    """This function return the logout
    :returns: front logout of logout.html
    :rtype: html
    """
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")

    return render_template("index.html")
