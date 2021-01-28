#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False)
def all_Amenity():
    """ Task 9 """
    ls = []
    for st in storage.all("Amenity").values():
        ls.append(st.to_dict())
    return jsonify(ls)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def retrive_Amenity(amenity_id):
    """ Task 9 """
    ame = storage.get("Amenity", amenity_id)
    if ame is None:
        abort(404)
    return jsonify(ame.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_Amenity(amenity_id):
    """ Task 9 """
    to_del = storage.get("Amenity", amenity_id)
    if to_del:
        storage.delete(to_del)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_Amenity(amenity_id=None):
    """ Task 9 """
    to_update = storage.get("Amenity", amenity_id)
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


@app_views.route('/amenities/', methods=['POST'], strict_slashes=False)
def post_amenity():
    """create a new amenitie"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "name" not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    new_state = Amenity(**request.get_json())
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)
