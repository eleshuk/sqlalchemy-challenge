from flask import Flask
from flask import jsonify

import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)

# Define what to do when a user hits the index route

@app.route("/")
def home():
    print("")
