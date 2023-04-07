from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6129647312:AAG9o2G4-4rctiIbiTvDgWKIKApKIXWwnlc")
API_ID = int(os.environ.get("API_ID", "7111812"))
API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "SongsDownloaderTgBot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
