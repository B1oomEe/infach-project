from flask import request, jsonify
from app import app, db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from models import User

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify({'token': access_token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    return jsonify({'tasks': ['Task 1', 'Task 2', 'Task 3']})

@app.route('/tasks/solve', methods=['POST'])
@jwt_required()
def solve_task():
    data = request.get_json()
    return jsonify({'message': f'Task {data["task_id"]} solved'})