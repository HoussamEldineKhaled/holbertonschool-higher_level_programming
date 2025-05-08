#!/usr/bin/python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28,
                  "city": "Los Angeles"},
         "john": {"name": "John", "age": 30,
                  "city": "New York"}}
@app.route('/')

def home():
    return "Welcome to the Flask API!"

@app.route('/data')

def fill_Data():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
