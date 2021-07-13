#!/usr/bin/env python
import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import sys


app = Flask(__name__)
CORS(app)

if(len(sys.argv) < 2):
    print('\nDatabase URI is missing!\n\n')
app.config['SQLALCHEMY_DATABASE_URI'] = sys.argv[1]

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
