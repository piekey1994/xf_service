from sql_config import db
import os
from flask import Flask
db.drop_all()
db.create_all()