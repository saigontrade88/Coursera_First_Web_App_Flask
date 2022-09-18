from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime
from models import Task
from datetime import datetime

import re
import forms



#decorated function
@app.route('/')
@app.route('/index')
def index():
    print('http://127.0.0.1:8580/about')
    tasks = Task.query.all()
    return render_template('index.html', current_title='Landing page', tasks=tasks)

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database')
        print('Submitted title', form.title.data) 
        return redirect(url_for('index'))
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