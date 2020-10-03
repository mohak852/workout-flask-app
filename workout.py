from flask import Flask, jsonify, request, session
import jwt
from model import db, User
import bcrypt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_current_user,
    get_jwt_identity
)
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "Super secret Key"
jwt = JWTManager(app)
@app.route("/")
def index():
    return jsonify({"Hello": "world"})

@app.route("/login" ,methods=['POST'])
def login():
    data = request.get_json()
    namedata = data['name']
    password = data['password']
    print(data)
    user = User.query.filter_by(name=namedata).first()
    print(user)
    print(bcrypt.hashpw(password, user.password_hash))
    print(user.password_hash)
    if user is not None:
        if bcrypt.hashpw(password, user.password_hash) == user.password_hash:
            access_token = create_access_token(identity=namedata)
            return jsonify(access_token=access_token), 200
        return jsonify({"message": "Invalid password"})
    return jsonify({"message": "Register First !!"})


@app.route("/pro")
@jwt_required
def pro():
    current_user = get_jwt_identity()
    nameofuser = str(current_user)
    user = User.query.filter_by(name=nameofuser).first()
    user_data = {}
    user_data['name'] = user.name
    user_data['units'] = user.units
    return jsonify(logged_in_as=user_data), 200

if __name__ == "__main__":
    app.debug = True
    app.run()
