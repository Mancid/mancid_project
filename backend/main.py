from flask import Blueprint, render_template
from flask_login import login_required, current_user


MAIN = Blueprint('main', __name__)


@MAIN.route('/')
def index():
  """Returns page login.html

  :returns: page login.html
  :rtype: html
  """
  return render_template('index.html')


@MAIN.route('/profile')
@login_required
def profile():
  """Returns page profile.html with name and email of the user
  
  :returns: page profile.html
  :rtype: html
  """
  return render_template('profile.html', name=current_user.name,
                         mail=current_user.email)
