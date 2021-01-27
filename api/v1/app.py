#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ Task 4 """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Task 6"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', default=5000),
            threaded=True)
