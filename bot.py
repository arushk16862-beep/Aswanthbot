import sys
import asyncio
import importlib.util
import logging
import logging.config
import pytz
from pathlib import Path
from datetime import date, datetime

# ---------------- LOGGING ----------------
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)

# ---------------- IMPORTS ----------------
from pyrogram import idle
from aiohttp import web
import aiohttp

from info import *
from utils import temp
from Script import script
from database.users_chats_db import db

from plugins import web_server
from plugins.clone import restart_bots

from Neon.bot import NeonBot
from Neon.bot.clients import initialize_clients
from Neon.util.keepalive import ping_server

# ---------------- KEEP ALIVE ----------------
async def keep_alive():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Keep-alive ping sent")
            except Exception as e:
                logging.error(f"Keep-alive error: {e}")
            await asyncio.sleep(100)

# ---------------- PLUGIN LOADER ----------------
def get_all_plugin_files(root="plugins"):
    files = []
    for path in Path(root).rglob("*.py"):
        if path.name != "__init__.py":
            files.append(path)
    return files

PLUGIN_FILES = get_all_plugin_files()

# ============================================================
#                     BOT START FUNCTION
# ============================================================
async def start_bot():
    print("\n🚀 Initializing Your Bot...\n")

    # ---- START BOT (ONLY ONCE) ----
    try:
        await NeonBot.start()
    except Exception as e:
        logging.error(f"Bot start failed: {e}")
        raise e

    await initialize_clients()

    # ---- LOAD PLUGINS ----
    for plugin in PLUGIN_FILES:
        try:
            name = plugin.stem
            spec = importlib.util.spec_from_file_location(name, plugin)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            sys.modules[name] = mod
            print(f"✅ Loaded plugin: {name}")
        except Exception as e:
            logging.error(f"Plugin load failed {plugin}: {e}")

    # ---- KEEP ALIVE ----
    if ON_HEROKU:
        asyncio.create_task(ping_server())

    if KEEP_ALIVE_URL:
        asyncio.create_task(keep_alive())

    # ---- LOAD BANS ----
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats

    # ---- BOT INFO ----
    me = await NeonBot.get_me()
    temp.BOT = NeonBot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name

    logging.info(script.LOGO)

    # ---- RESTART MESSAGE ----
    tz = pytz.timezone("Asia/Kolkata")
    today = date.today()
    time = datetime.now(tz).strftime("%I:%M:%S %p")

    try:
        await NeonBot.send_message(
            LOG_CHANNEL,
            script.RESTART_TXT.format(me.first_name, today, time),
        )
    except Exception as e:
        logging.warning(f"Restart message failed: {e}")

    # ---- CLONE MODE ----
    if CLONE_MODE:
        print("♻ Restarting clone bots...")
        await restart_bots()

    # ---- WEB SERVER ----
    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", PORT).start()

    print("✅ Bot Started Successfully!")
    await idle()

# ============================================================
#                          MAIN
# ============================================================
if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("👋 Bot stopped")
