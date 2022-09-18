'''
https://code.visualstudio.com/docs/python/tutorial-flask
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__) # print(__name__)
app.config['SECRET_KEY'] = 'cpr4llp' #need to update it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  \
                                        os.path.join(BASE_DIR, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from route import *

if __name__ == '__main__':
    app.run(port=8580, debug=True)
    