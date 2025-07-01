"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa

This program is free software: you can redistribute it and can modify
as you want or you can collab if you have new ideas.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")

try:
    mongo_client = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = mongo_client["Alexa"]  # or use .get_database() if dynamic
    db = mongo_client["subscriptions"]  # Your second DB
    LOGGER(__name__).info("Connected to your Mongo Database.")
except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to your Mongo Database: {e}")
    exit()

# Export client if needed elsewhere
MONGODB_CLI = mongo_client