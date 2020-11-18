#!/usr/bin/env python3
""" a basic Flask app. """
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """ returns a message when the route / is requested """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    """ registers a new user """
    email = request.form.get('email')
    print("REQUUEEEEEESSSSSSSSSST", request.form.get('email'))
    return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
