#!/usr/bin/python3
""" Task 4 """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def all_states():
    """ Task 4 """
    return jsonify(status="OK")
