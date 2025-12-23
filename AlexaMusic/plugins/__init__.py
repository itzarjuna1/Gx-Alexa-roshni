# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import glob
import os

BASE_DIR = os.path.dirname(__file__)

ALL_MODULES = sorted(
    [
        os.path.splitext(os.path.basename(file))[0]
        for file in glob.glob(os.path.join(BASE_DIR, "*.py"))
        if not file.endswith("__init__.py")
    ]
)

__all__ = ALL_MODULES + ["ALL_MODULES"]
