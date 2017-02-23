from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite') 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Plugin(db.Model):
    __tablename__ = 'plugin'
    unicode = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64),unique=True)
    info = db.Column(db.Text)
    author = db.Column(db.String(64))
    pushtime = db.Column(db.DateTime)
    location = db.Column(db.String(64))
    coverage = db.Column(db.Integer)