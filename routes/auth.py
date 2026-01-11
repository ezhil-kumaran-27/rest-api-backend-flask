from flask import request, Blueprint
from models.user import User
from database.db import db

auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    user = User(
        email=data['email'],
        password = data['password']
    )
    db.session.add(user)
    db.session.commit()

    return{'message': "User Registered Successfully"},201