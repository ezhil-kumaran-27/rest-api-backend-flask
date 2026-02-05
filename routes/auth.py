from flask import request, Blueprint,jsonify
from models.user import User
from database.db import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint("auth",__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    user = User(
        email=data['email'],
        password = data['password']
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': "User Registered Successfully"}),201

@auth_bp.route("/login",methods = ["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password,data["password"]):
        return {"error": "Invalid email or password"},401
    access_token = create_access_token(identity=user.id)

    return{
        "message":"Login successful",
        "access_token":access_token

    }

@auth_bp.route("/profile",methods = ["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return{
        "id": user.id,
        "email": user.email,

    }
