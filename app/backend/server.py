#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer

Backend: Main app.
"""
import os
import sys

import flask

from home.home import home_page

print(sys.path)

app = flask.Flask(__name__, static_folder="ui",
                  static_url_path="/data/", template_folder=os.path.abspath("./app/frontend/"))

app.add_url_rule("/", view_func=home_page)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
