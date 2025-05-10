#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users =  {
    "barry": generate_password_hash("all8"),
    "nagham": generate_password_hash("jfd")
}



@auth.login_required
