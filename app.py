# Initial Import of Dependencies
import os
import json
from flask import Flask , render_template, jsonify, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import connection_string
from decimal import Decimal

app = Flask(__name__)

# Connecting to database
engine = create_engine(connection_string)

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

# Creating home route
@app.route('/')
def home():
    return render_template("index.html")

# Office hours connect 
@app.route("/api/results>")
def results():
    connection = engine.connect()
    query = connection.execute(f"SELECT * FROM learning_survey_results")
    obj = [{column: value for column, value in rowproxy.items()} for rowproxy in query]
    return json.dumps(obj, cls=JSONEncoder)