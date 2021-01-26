#!/usr/bin/python3
""" Task 4 """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


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
    app.run()
