from flask import Flask, jsonify, request
import user_controller
from db import create_tables

app = Flask(__name__)


@app.route('/users', methods=["GET"])
def get_users():
    users = user_controller.get_users()
    return jsonify(users)


@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    name = user_details["name"]
    email = user_details["email"]
    phone = user_details["phone"]
    result = user_controller.insert_user(name, email, phone)
    return jsonify(result)


@app.route("/user", methods=["PUT"])
def update_user():
    user_details = request.get_json()
    id = user_details["id"]
    name = user_details["name"]
    email = user_details["email"]
    phone = user_details["phone"]
    result = user_controller.update_user(id, name, email, phone)
    return jsonify(result)


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = user_controller.delete_user(id)
    return jsonify(result)


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    user = user_controller.get_by_id(id)
    return jsonify(user)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
