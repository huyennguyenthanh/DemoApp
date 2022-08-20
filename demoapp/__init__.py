from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('demoapp.config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()
from demoapp import routes
from demoapp import models
