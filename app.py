from flask import Flask,render_template,redirect,flash,url_for,request,session
from flask_sqlalchemy import SQLAlchemy
import os

# CONFIG
app=Flask(__name__)
app.secret_key="rgndunes"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'rgndunes'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DATABASE MODELS

# FLASKFORM

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# MAIN
if __name__=='__main__':
    app.run(debug=True)