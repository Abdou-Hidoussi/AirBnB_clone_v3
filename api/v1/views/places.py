#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<string:city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """task 10 get place from specific city"""
    cities = storage.get("City", city_id)
    if cities is None:
        abort(404)
    places = []
    for place in cities.places:
        cities.append(place.to_dict())
    return jsonify(places)


@app_views.route('/places/<place_id>', strict_slashes=False)
def retrive_Place(place_id):
    """ Task 10 """
    for ct in storage.all("Place").values():
        if ct.id == place_id:
            return jsonify(ct.to_dict())
    abort(404)


@app_views.route('/cities/<string:city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_Place(city_id):
    """Task 10 create place in city"""
    cities = storage.get("City", city_id)
    if cities is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    if "user_id" not in request.get_json():
        return make_response(jsonify({'error': 'Missing user_id'}), 400)

    kwargs = request.get_json()
    user = storage.get("User", kwargs['user_id'])
    if not user:
        abort(404)

    if 'name' not in kwargs:
        abort(400, "Missing name")

    kwargs['city_id'] = city_id

    place = Place(**kwargs)
    place.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
def put_Place(place_id):
    """update a place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'city_id',
                        'created_at', 'updated_at']:
            setattr(place, attr, val)
    place.save()
    return jsonify(place.to_dict())


@app_views.route('/places/<string:place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Place(place_id):
    """task 10 deletes a place from it's id"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return (jsonify({}))
