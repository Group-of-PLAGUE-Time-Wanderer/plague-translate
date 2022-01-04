#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer - Translate

Backend: Home page
"""
from flask import render_template


def home_page():
    return render_template("./home/home.html")
