#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLAGUE: Time Wanderer - Translate

Backend: Favicon
"""
from flask import redirect


def mstile():
    return redirect("/ui/favicon/assets/mstile-150x150.png")


def favicon16():
    return redirect("/ui/favicon/assets/favicon-16x16.png")


def safari_pinned():
    return redirect("/ui/favicon/assets/safari-pinned-tab.svg")


def favicon():
    return redirect("/ui/favicon/assets/favicon.ico")


def favicon_image():
    return redirect("/ui/favicon/assets/favicon.png")


def webmanifest():
    return redirect("/ui/favicon/assets/site.webmanifest")


def apple_touch():
    return redirect("/ui/favicon/assets/apple-touch-icon.png")


def browser_config():
    return redirect("/ui/favicon/assets/browserconfig.xml")


def android_chrome():
    return redirect("/ui/favicon/assets/android-chrome-72x72.png")


def favicon32():
    return redirect("/ui/favicon/assets/favicon-32x32.png")
