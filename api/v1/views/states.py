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


@app_views.route('/states/<state_id>', methods=['GET'])
def findSt(state_id):
    """ Task 7 """
    if state_id is not None:
        for st in storage.all("State").values():
            if st.id is state_id:
                return jsonify(st.to_dict())
    abort(404)
