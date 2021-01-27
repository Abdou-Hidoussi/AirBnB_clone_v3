#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage


@app_views.route('/cities/<city_id>', strict_slashes=False)
def retrive_City(city_id):
    """ Task 7 """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_City(city_id):
    """ Task 7 """
    to_del = storage.get("City", city_id)
    if to_del:
        storage.delete(to_del)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_City(city_id=None):
    """ Task 7 """
    to_update = storage.get("City", city_id)
    req = request.get_json()

    if to_update is None:
        abort(404)

    if req is None:
        abort(400)

    for key, value in req.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(to_update, key, value)

    storage.save()
    return jsonify(to_update.to_dict())
