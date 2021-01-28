#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from models.reviews import Reviews



@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_review(place_id):
    """task 12 get review from specific place"""
    places = storage.get("Place", place_id)
    if places is None:
        abort(404)
    reviews = []
    for reviews in places.reviews:
        reviews.append(place.to_dict())
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def retrive_Review(review_id):
    """ Task 12 """
    for ct in storage.all("Review").values():
        if ct.id == review_id:
            return jsonify(ct.to_dict())
    abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_Review(place_id):
    """Task 12 create review in place"""
    Places = storage.get("Place", place_id)
    if Places is None:
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

    if 'text' not in kwargs:
        abort(400, "Missing text")

    kwargs['place_id'] = Places.id

    rev = Review(**kwargs)
    rev.save()
    return make_response(jsonify(rev.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_Place(review_id):
    """update a review"""
    rev = storage.get("Review", review_id)
    if rev is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'place_id',
                        'created_at', 'updated_at']:
            setattr(rev, attr, val)
    rev.save()
    return jsonify(rev.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Review(review_id):
    """task 12 deletes a review from it's id"""
    rev = storage.get("Review", review_id)
    if rev is None:
        abort(404)
    rev.delete()
    storage.save()
    return (jsonify({}))
