from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
