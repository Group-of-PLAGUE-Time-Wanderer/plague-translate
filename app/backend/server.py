#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer

Backend: Main app.
"""
import os
import sys

import flask

from favicon.favicon import (
    android_chrome,
    apple_touch,
    browser_config,
    favicon,
    favicon16,
    favicon32,
    favicon_image,
    mstile,
    safari_pinned,
    webmanifest,
)
from home.home import home_page

print(sys.path)
print(os.getcwd())

app = flask.Flask(
    __name__,
    template_folder=os.path.abspath("./app/frontend/"),
    static_folder=os.path.abspath("./ui/"),
)

app.add_url_rule("/", view_func=home_page)

app.add_url_rule("/mstile-150x150.png", view_func=mstile)
app.add_url_rule("/favicon.ico", view_func=favicon)
app.add_url_rule("/favicon.png", view_func=favicon_image)
app.add_url_rule("/favicon-16x16.png", view_func=favicon16)
app.add_url_rule("/safari-pinned-tab.svg", view_func=safari_pinned)
app.add_url_rule("/site.webmanifest", view_func=webmanifest)
app.add_url_rule("/apple-touch-icon.png", view_func=apple_touch)
app.add_url_rule("/browserconfig.xml", view_func=browser_config)
app.add_url_rule("/android-chrome-72x72.png", view_func=android_chrome)
app.add_url_rule("/favicon-32x32.png", view_func=favicon32)


@app.route("/dev/url_for")
def url_for():
    return flask.url_for("static", filename="favicon/assets/favicon.ico")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
