# Copyright (C) 2025 by Alexa_Help @ Github
# https://github.com/TheTeamAlexa

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
"""

# =======================
# 🔥 HARD EVENT LOOP FIX
# =======================
import asyncio
import sys

# Force default loop (Pyrogram-safe)
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
asyncio.set_event_loop(asyncio.new_event_loop())

# =======================
# Normal Imports
# =======================
from AlexaMusic.core.bot import AlexaBot
from AlexaMusic.core.dir import dirr
from AlexaMusic.core.git import git
from AlexaMusic.core.userbot import Userbot
from AlexaMusic.misc import dbb, heroku
from .logging import LOGGER

# =======================
# Startup Tasks
# =======================

# Directories
dirr()

# Git check
git()

# Database
dbb()

# Heroku config
heroku()

# =======================
# Clients (IMPORTANT ORDER)
# =======================

# Bot Client
app = AlexaBot()

# Assistant Client
userbot = Userbot()

# =======================
# Platforms
# =======================
from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

LOGGER(__name__).info("AlexaMusic Bot Initialized Successfully")
