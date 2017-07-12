from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)

import models
db.create_all()

import views
