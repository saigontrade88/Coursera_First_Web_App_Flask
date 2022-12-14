from app import app
from flask import render_template
from datetime import datetime
import re
import forms


#decorated function
@app.route('/')
@app.route('/index')
def index():
    print('http://127.0.0.1:8580/about')
    return render_template('index.html', current_title='Landing page')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about.html', 
                                form=form, 
                                title=form.title.data)
    return render_template('about.html', 
                            current_title='About page',
                            form=form)

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    print('http://127.0.0.1:5000/hello/vscode')
    return content