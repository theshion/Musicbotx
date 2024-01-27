from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic.core.call import Anony
from AnonXMusic import Spotify, app, LOGGER

SPOTIFY_PLAYLISTS = {
    'English': 'hCVorPfNT8Ci_Uhzicx8qA',
    'Hindi': 'pTIt8-UhQ7OebaiCt5wM7A',
    'OtherLanguages': 'VhIgr9TXRIa9_FJGgGr99A'
}


@app.on_message(filters.command("aiplay"))
def aiplayl(_, msg):
    try:
        chat_id = msg.chat.id

        buttons = [
            [InlineKeyboardButton(name, callback_data=name) for name in SPOTIFY_PLAYLISTS.keys()]
        ]
        msg.reply_text("Choose from the buttons below:", reply_markup=InlineKeyboardMarkup(buttons))

    except Exception as e:
        LOGGER("AnonXMusic").error(f"Error in aiplay command: {e}")
        msg.reply_text("An error occurred while processing your request.")

@app.on_callback_query(filters.regex("English|Hindi|OtherLanguages"))
def butston_callback(_, callback_query):
    try:
        chat_id = callback_query.message.chat.id
        user_id = callback_query.from_user.id
        playlist_name = callback_query.data

        playlist_id = SPOTIFY_PLAYLISTS.get(playlist_name)

        if not playlist_id:
            raise ValueError(f"Invalid playlist: {playlist_name}")

        playlist_tracks = Spotify.playlist_tracks(playlist_id)
        track_url = playlist_tracks['items'][0]['track']['external_urls']['Spotify']

        Anony.stream_call(chat_id, user_id, audio_file=track_url)
        callback_query.message.reply_text(f"Ai-player started\nNow playing {playlist_name}\nQuery by {callback_query.from_user.mention}\nStreamed by Noah Music")

    except Exception as e:
        LOGGER("AnonXMusic").error(f"Error in button callback: {e}")
        callback_query.message.reply_text("An error occurred while processing your request.")
