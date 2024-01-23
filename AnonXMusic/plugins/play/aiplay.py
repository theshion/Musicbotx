import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import seconds_to_min, time_to_seconds
from AnonXMusic.utils.channelplay import get_channeplayCB
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.decorators.play import PlayWrapper
from AnonXMusic.utils.formatters import formats
from AnonXMusic.utils.inline import (
    botplaylist_markup,
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from AnonXMusic.utils.logger import play_logs
from AnonXMusic.utils.stream.stream import stream
from config import BANNED_USERS, lyrical


@app.on_message(filters.command("aiplay"))
async def aiplay_command(client, message):
    buttons = [
        [
            InlineKeyboardButton("English", callback_data="aiplay:english"),
            InlineKeyboardButton("Hindi", callback_data="aiplay:hindi"),
            InlineKeyboardButton("Phonk", callback_data="aiplay:phonk"),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await message.reply_text("Choose a playlist:", reply_markup=keyboard)

# Assuming you have the necessary functions for playing Spotify playlists in your AnonXMusic module

@app.on_callback_query(filters.regex("aiplay:"))
async def aiplay_callback(client, callback_query):
    playlist_type = callback_query.data.split(":")[1]
    spotify_url = get_spotify_url_for_playlist(playlist_type)  # Replace with your logic to get Spotify URLs
    if not spotify_url:
        return
    await play_spotify_playlist(callback_query.from_user.id, spotify_url)

# Replace the functions below with your actual implementations for Spotify URL retrieval and playlist playback
def get_spotify_url_for_playlist(playlist_type):
    # Replace with your logic to map playlist types to Spotify URLs
    if playlist_type == "english":
        return "https://open.spotify.com/playlist/0rAdSPycrFdaBXh9xSW3ap?si=hCVorPfNT8Ci_Uhzicx8qA"
    elif playlist_type == "hindi":
        return "https://open.spotify.com/playlist/0XSjIw422sAwiKUMq4cm2l?si=pTIt8-UhQ7OebaiCt5wM7A"
    elif playlist_type == "phonk":
        return "https://open.spotify.com/artist/3kXvE7gEBfGkwDaknMngF7?si=VhIgr9TXRIa9_FJGgGr99A"
    else:
        return None

async def play_spotify_playlist(user_id, spotify_url):
    # Replace with your logic to play Spotify playlists
    try:
        # Call the function from your AnonXMusic module to play Spotify playlist
        await Anony.stream_call(spotify_url)
    except Exception as e:
        print(f"Error playing playlist: {e}")
