from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from demoapp.createtable import UserModel, db
from flask import jsonify
app = Flask(__name__)


def create_app():
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    # initializing bcrypt and db
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        items = []
        for item in db.session.query(UserModel).all():
            del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
        return (items)

    return app


app = create_app()
