#!/usr/bin/python3
"""
Restful Api
"""

from api.v1.views import app_views
import json


@app_views.route("/status")
def ret_status():
    string = json.dumps({"status": "OK"})
    return "{}".format(string)
