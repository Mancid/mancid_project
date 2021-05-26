# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, DB, url


AUTH = Blueprint('auth', __name__)


@AUTH.route('/login')
def login():
  """Returns page login.html"""
  return render_template('login.html')


@AUTH.route('/login', methods=['POST'])
def login_post():
  """
  This function return page login.html
  If not user : try again
  If user : return page parking.html
  """
  email = request.form.get('email')
  password = request.form.get('password')
  remember = True if request.form.get('remember') else False

  user = DB.query(User).filter_by(email=email).first()

  # check if user actually exists
  # take the user supplied password, hash it,
  # and compare it to the hashed password in database
  if not user or not check_password_hash(user.password, password):
    flash('Please check your login credentials and try again.')
    # if user doesn't exist or password is wrong, reload the page
    return redirect(url_for('auth.login'))

  # if the above check passes, then we know the user has the right credentials
  login_user(user, remember=remember)
  flash('You have been logged in.')
  return redirect(url_for('main.parking'))


@AUTH.route('/signup')
def signup():
  """Returns page signup.html"""
  return render_template('signup.html')


@AUTH.route('/signup', methods=['POST'])
def signup_post():
  """
  This function create a user with email, name and password.
  The user is recorde in the database.
  """
  email = request.form.get('email')
  name = request.form.get('name')
  password = request.form.get('password')

  user = DB.query(User).filter_by(email=email).first()
  # if this returns a user, then the email already exists in database

  if user:
    # if a user is found,
    # we want to redirect back to signup page so user can try again
    flash('Email address already exists')
    return redirect(url_for('auth.signup'))

  # create new user with the form data.
  # Hash the password so plaintext version isn't saved.
  new_user = User(email=email,
                  name=name,
                  password=generate_password_hash(password, method='sha256'))

  # add the new user to the database
  DB.add(new_user)
  DB.commit()

  # code to validate and add user to database goes here
  return redirect(url_for('auth.login'))


@AUTH.route('/logout')
@login_required
def logout():
  """
  This function logout the user.
  """
  logout_user()
  flash('You have been logged out.')
  return redirect(url_for('main.index'))
