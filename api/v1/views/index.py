#!/usr/bin/python3
"""
Restful Api
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status")
def ret_status():
    return jsonify(status="OK")
