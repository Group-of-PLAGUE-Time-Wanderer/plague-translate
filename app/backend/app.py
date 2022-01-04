#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer

Backend: Main app.
"""
import flask

app = flask.Flask(__name__, static_folder="ui",
                  static_url_path="data/", template_folder="app/frontend/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
