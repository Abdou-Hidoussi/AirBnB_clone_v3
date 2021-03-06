#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.city import City
from models.user import User


@app_views.route('/users', strict_slashes=False)
def all_User():
    """ Task 10 """
    ls = []
    for st in storage.all("User").values():
        ls.append(st.to_dict())
    return jsonify(ls)


@app_views.route('/users/<user_id>', strict_slashes=False)
def retrive_User(user_id):
    """ Task 10 """
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_User(user_id):
    """ Task 10 """
    to_del = storage.get("User", user_id)
    if to_del:
        storage.delete(to_del)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_User(user_id=None):
    """ Task 10 """
    to_update = storage.get("User", user_id)
    req = request.get_json()

    if to_update is None:
        abort(404)

    if req is None:
        abort(400)

    for key, value in req.items():
        if key not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(to_update, key, value)

    storage.save()
    return jsonify(to_update.to_dict())


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def post_user():
    """create a new user"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "email" not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if "password" not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    new_state = User(**request.get_json())
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)
