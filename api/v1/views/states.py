#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'])
def retrive_State():
    """ Task 7 """
    ls = []
    for st in storage.all("State").values():
        ls.append(st.to_dict())
    return jsonify(ls)
