from flask import Flask,render_template,redirect,flash,url_for,request,session
from flask_sqlalchemy import SQLAlchemy
import os
import smtplib, ssl
from datetime import date

# CONFIG
app=Flask(__name__)
app.secret_key="rgndunes"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'rgndunes'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DATABASE MODELS
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    subject = db.Column(db.String(250), unique=False, nullable=False)
    message = db.Column(db.String(500), unique=False, nullable=False)
    date = db.Column(db.String(50), unique=False, nullable=False)

# FLASKFORM

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/certificates', methods=['GET', 'POST'])
def certificates():
    return render_template('certificates.html')

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

@app.route('/hobby', methods=['GET', 'POST'])
def hobby():
    return render_template('hobby.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/contact/sendingFeedback', methods=['GET', 'POST'])
def sendingFeedback():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get('message')
        today = date.today()
        curr_date = today.strftime("%B %d, %Y")

        contactInfo = Contact(email=email, subject=subject, message=msg, date=str(curr_date))
        db.session.add(contactInfo)
        db.session.commit()

        try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            receiver_email = email  # Enter receiver address
            sender_email = "testingdunes@gmail.com"  # Enter your address
            password = "Duqo&@5200"
            message = """\
            Subject: Thank you for the feedback.

            We will reach out to you soon."""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            
            receiver_email = "testingdunes@gmail.com"
            message = """\
            Subject: Portfolio-v2.

Feedback from """ + email + """. \nMessage : """ + msg + """\nDate : """ + curr_date

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        except:
            return render_template('index.html')
    return render_template('index.html')

# MAIN
if __name__=='__main__':
    app.run(debug=True)