from flask import Flask, render_template, request, session, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
