from app import app
from flask import render_template
from datetime import datetime
import re
import forms
from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


#decorated function
@app.route('/')
@app.route('/landing-page')
def index():
    return render_template('landing-page.html', current_title='Landing page')


# Home page
############################################################
@app.route('/vn/home-page', methods=['GET', 'POST'])
def homeVN():
    return render_template('./vn/home-page.html', current_title='Home page')

@app.route('/lao/home-page', methods=['GET', 'POST'])
def homeLao():
    return render_template('./laos/home-page.html', current_title='Home page')

@app.route('/cam/home-page', methods=['GET', 'POST'])
def homeCam():
    return render_template('./cambodia/home-page.html', current_title='Home page')

@app.route('/china/home-page', methods=['GET', 'POST'])
def homeChina():
    return render_template('./china/home-page.html', current_title='Home page')
############################################################


# About page
############################################################
@app.route('/vn/about-page', methods=['GET', 'POST'])
def aboutVN():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)

@app.route('/lao/about-page', methods=['GET', 'POST'])
def aboutLao():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)

@app.route('/cam/about-page', methods=['GET', 'POST'])
def aboutCam():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)

@app.route('/china/about-page', methods=['GET', 'POST'])
def aboutChina():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about-page.html', form=form, title=form.title.data)
    return render_template('about-page.html', current_title='About page', form=form)
############################################################






# @app.route("/hello/<name>")
# def hello_there(name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     print('http://127.0.0.1:5000/hello/vscode')
#     return content