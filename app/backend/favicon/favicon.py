#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer - Translate

Backend: Favicon
"""
from flask import redirect


def mstile():
    return redirect("/data/favicon/assets/mstile-150x150.png")


def favicon16():
    return redirect("/data/favicon/assets/favicon-16x16.png")


def safari_pinned():
    return redirect("/data/favicon/assets/safari-pinned-tab.svg")


def favicon():
    return redirect("/data/favicon/assets/favicon.ico")


def favicon_image():
    return redirect("/data/favicon/assets/favicon.png")


def webmanifest():
    return redirect("/data/favicon/assets/site.webmanifest")


def apple_touch():
    return redirect("/data/favicon/assets/apple-touch-icon.png")


def browser_config():
    return redirect("/data/favicon/assets/browserconfig.xml")


def android_chrome():
    return redirect("/data/favicon/assets/android-chrome-72x72.png")


def favicon32():
    return redirect("/data/favicon/assets/favicon-32x32.png")
