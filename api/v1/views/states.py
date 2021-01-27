#!/usr/bin/python3
""" Task 4 """
from flask import Flask, Blueprint, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def all_State():
    """ Task 7 """
    ls = []
    for st in storage.all("State").values():
        ls.append(st.to_dict())
    return jsonify(ls)


@app_views.route('/states/<state_id>', strict_slashes=False)
def retrive_State(state_id):
    """ Task 7 """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_State(state_id):
    """ Task 7 """
    to_del = storage.get("State", state_id)
    if to_del:
        storage.delete(to_del)
        storage.save()
        return jsonify({})
    abort(404)
