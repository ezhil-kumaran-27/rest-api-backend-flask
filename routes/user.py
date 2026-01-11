from flask import Blueprint, request
from models.user import User
from database.db import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/user',methods=['POST'])
def create_user():
    data = request.json
    user = User(email=data['email'],password=data['password'])
    db.session.add(user)
    db.session.commit()
    return{"message":"User Created Successfully"}
