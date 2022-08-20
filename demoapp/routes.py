from demoapp import app
from demoapp import db
from demoapp.createtable import UserModel
from demoapp.models import *
from flask import jsonify
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return {200: "OK"}


@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)


@app.route('/items', methods=['GET'])
def get_items():
    items = []
    for item in db.session.query(UserModel).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


@app.route('/items', methods=['POST'])
def create_item():
    body = request.get_json()
    db.session.add(Item(body['title'], body['content']))
    db.session.commit()
    return "item created"


@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    db.session.query(Item).filter_by(id=id).update(
        dict(title=body['title'], content=body['content']))
    db.session.commit()
    return "item updated"


@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    db.session.query(Item).filter_by(id=id).delete()
    db.session.commit()
    return "item deleted"
