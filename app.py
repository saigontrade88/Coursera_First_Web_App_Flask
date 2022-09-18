'''
https://code.visualstudio.com/docs/python/tutorial-flask
'''
from flask import Flask

app = Flask(__name__) # print(__name__)
app.config['SECRET_KEY'] = 'cpr4llp' #need to update it

from route import *

if __name__ == '__main__':
    app.run(port=8580, debug=True)
    