# Copyright (C) 2025 by Alexa_Help
# https://github.com/TheTeamAlexa

import asyncio
import sys

# Ensure event loop exists (Python 3.10+ fix)
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus

import config
from ..logging import LOGGER


class AlexaBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            max_concurrent_transmissions=5,
        )
        LOGGER(__name__).info("Starting Bot...")

    async def start(self):
        await super().start()

        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.mention = get_me.mention

        # 🔕 LOG GROUP CHECK (NON-FATAL)
        if config.LOG_GROUP_ID:
            try:
                await self.send_message(
                    config.LOG_GROUP_ID,
                    "» ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ, ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀssɪsᴛᴀɴᴛ..."
                )

                member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
                if member.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).warning(
                        "Bot is not admin in log group. Logging will be limited."
                    )

            except Exception as e:
                LOGGER(__name__).warning(
                    f"Log group not accessible, skipping logs. Reason: {e}"
                )
        else:
            LOGGER(__name__).warning("LOG_GROUP_ID not set. Skipping log group checks.")

        # Bot name
        if get_me.last_name:
            self.name = f"{get_me.first_name} {get_me.last_name}"
        else:
            self.name = get_me.first_name

        LOGGER(__name__).info(f"MusicBot Started Successfully as {self.name}")
