import time
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import xmlrpc.client
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

cors = CORS(app)

@app.route('/time')
def get_current_time():
    print(time.time())
    return {'time': datetime.fromtimestamp(time.time())}

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

if __name__ == '__main__':
   app.run(debug = True)