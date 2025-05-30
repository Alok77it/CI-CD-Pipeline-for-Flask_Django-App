from flask import Flask

app = Flask(__name__)

users = {"admin": "password"}

from app import routes
