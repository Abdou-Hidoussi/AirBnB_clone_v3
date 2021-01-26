#!/usr/bin/python3
""" Task 4 """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def all_states():
    """ Task 4 """
    return jsonify(status="OK")


@app_views.route('/stats')
def stat_count():
    """ Task 5 """
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count_stats)
