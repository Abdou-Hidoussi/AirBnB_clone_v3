#!/usr/bin/python3
"""
Task 13
"""
from api.v1.views import app_views, Review, storage
from flask import abort, jsonify, request


@app_views.route("/places/<place_id>/reviews", methods=["GET"],
                 strict_slashes=False)
def all_reviews(place_id):
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    reviews = []
    for review in place.reviews:
        review.append(reviews.to_dict())
    return jsonify(reviews)

    