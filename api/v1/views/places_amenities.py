#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
import os


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities(place_id):
    """task 14"""
    places = storage.get("Place", place_id)
    if places is None:
        abort(404)
    amenities = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenity_objects = places.amenities
    else:
        amenity_objects = places.amenity_ids
    for am in amenity_objects:
        amenities.append(am.to_dict())
    return jsonify(amenities)

@app_views.route('/places/<string:place_id>/amenities/<string:amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    place = storage.get("Place", place_id)
    if (place is None) or (amenity_id is None):
        abort(404)
    if amenity_id not in place.amenities_id:
        abort(404)
    else:
        place.amenities_id.remove(amenity_id)
        place.save()
    return (jsonify({}))
