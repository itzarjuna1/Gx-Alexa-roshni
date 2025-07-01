# Copyright (C) 2021-2025 by Team Alexa
# Modified & Cleaned by ChatGPT for @Dhruv_Gc

import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load .env variables
load_dotenv()

# ✅ Utility functions
def to_bool(value): return str(value).lower() in ("true", "1", "yes")

def validate_url(name, url):
    if url and not url.startswith("https://"):
        print(f"[ERROR] - {name} must start with https://")
        sys.exit()

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# ✅ Mandatory Config
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "0"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "0"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ✅ Bot Identity
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "AlexaMusicBot")

# ✅ Optional & Feature Toggles
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = to_bool(getenv("AUTO_LEAVING_ASSISTANT", "False"))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_SUGGESTION_MODE = to_bool(getenv("AUTO_SUGGESTION_MODE", "False"))
AUTO_DOWNLOADS_CLEAR = to_bool(getenv("AUTO_DOWNLOADS_CLEAR", "True"))
PRIVATE_BOT_MODE = to_bool(getenv("PRIVATE_BOT_MODE", "False"))

# ✅ Sessions
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

# ✅ Heroku & Git
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")
GIT_TOKEN = getenv("GIT_TOKEN", "")

# ✅ Support Links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/who_cares_qt")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Destiny_Infinity_Og")

# ✅ Size & Limit Controls
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# ✅ Third-party Integrations
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
COOKIES = getenv("COOKIES", "")

# ✅ Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/d593c6064ff7657d0c714.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "assets/Ping.jpeg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "assets/Playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "assets/Global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "assets/Stats.jpeg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "assets/Audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "assets/Video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "assets/Stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "assets/Soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "assets/Youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "assets/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "assets/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "assets/SpotifyPlaylist.jpeg")

# ✅ Duration Conversion
DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
SONG_DOWNLOAD_DURATION_LIMIT = time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")

# ✅ Validate Critical URLs
validate_url("SUPPORT_CHANNEL", SUPPORT_CHANNEL)
validate_url("SUPPORT_GROUP", SUPPORT_GROUP)
validate_url("UPSTREAM_REPO", UPSTREAM_REPO)
validate_url("GITHUB_REPO", GITHUB_REPO)

# ✅ Optional Image URL checks
for name, url in {
    "PING_IMG_URL": PING_IMG_URL,
    "PLAYLIST_IMG_URL": PLAYLIST_IMG_URL,
    "GLOBAL_IMG_URL": GLOBAL_IMG_URL,
    "STATS_IMG_URL": STATS_IMG_URL,
    "TELEGRAM_AUDIO_URL": TELEGRAM_AUDIO_URL,
    "TELEGRAM_VIDEO_URL": TELEGRAM_VIDEO_URL,
    "STREAM_IMG_URL": STREAM_IMG_URL,
    "SOUNCLOUD_IMG_URL": SOUNCLOUD_IMG_URL,
    "YOUTUBE_IMG_URL": YOUTUBE_IMG_URL,
}.items():
    if url and not url.startswith("https://") and "assets/" not in url:
        print(f"[ERROR] - {name} is invalid. Must start with https:// or be a local asset.")
        sys.exit()

# ✅ Runtime Constants
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"

# ✅ Runtime Caches
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []