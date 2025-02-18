from werkzeug.security import generate_password_hash, check_password_hash
from db.database import SessionLocal
from .models import User
import json


def register_user(data):
    session = SessionLocal()
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], email=data['email'], hashed_password=hashed_password, role='student')
    session.add(user)
    session.commit()
    session.close()
    return json.dump({"message": "User registered successfully"}), 201

def login_user(data):
    session = SessionLocal()
    user = session.query(User).filter_by(email=data['email']).first()
    if user and check_password_hash(user.hashed_password, data['password']):
        return json.dump({"message": "Login successful"}), 200
    return json.dump({"error": "Invalid credentials"}), 401
