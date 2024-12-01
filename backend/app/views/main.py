from flask import jsonify, request
from app import app, db
from app.models.user import User

def index():
    return jsonify({"message": "Hello from Flask!"})

def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])

def add_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})
