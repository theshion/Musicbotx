from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic.core.call import Anony
from AnonXMusic import spotify, app
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_PLAYLISTS = {
    'English': 'https://open.spotify.com/playlist/0rAdSPycrFdaBXh9xSW3ap?si=hCVorPfNT8Ci_Uhzicx8qA',
    'Hindi': 'https://open.spotify.com/playlist/0XSjIw422sAwiKUMq4cm2l?si=pTIt8-UhQ7OebaiCt5wM7A',
    'OtherLanguages': 'https://open.spotify.com/artist/3kXvE7gEBfGkwDaknMngF7?si=VhIgr9TXRIa9_FJGgGr99A'
}


@app.on_message(filters.command("aiplay"))
def aiplay(_, msg):
    try:
        chat_id = msg.chat.id
        user_id = msg.from_user.id

        # Create buttons for different playlists
        buttons = [
            [
                InlineKeyboardButton("English", callback_data='English'),
            ],
            [
                InlineKeyboardButton("Hindi", callback_data='Hindi'),
            ],
            [
                InlineKeyboardButton("Other Languages", callback_data='OtherLanguages')
            ]
        ]

        # Send the buttons to the user
        msg.reply_text("ᴄʜᴏᴏꜱᴇ ꜰʀᴏᴍ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ", reply_markup=InlineKeyboardMarkup(buttons))

    except Exception as e:
        print(f"Error: {e}")
        msg.reply_text("An error occurred while processing your request.")

@app.on_callback_query()
def button_callback(_, callback_query):
    try:
        chat_id = callback_query.message.chat.id
        user_id = callback_query.from_user.id
        playlist_name = callback_query.data

        # Get the playlist ID based on the user's choice
        playlist_id = SPOTIFY_PLAYLISTS.get(playlist_name)

        # Get the first track from the selected Spotify playlist
        playlist_tracks = spotify.playlist_tracks(playlist_id)
        track_url = playlist_tracks['items'][0]['track']['external_urls']['spotify']

        # Start playing the track on the voice chat
        Anony.join_group_call(chat_id, user_id, audio_file=track_url)
        callback_query.message.reply_text(f"➲ <u>ᴀɪ-ᴘʟᴀʏᴇʀ ꜱᴛᴀʀᴛᴇᴅ</u>\n⬝ ɴᴏᴡ ᴘʟᴀʏɪɴɢ {playlist_name}\n⬝ ợᴜᴇʀʏ ʙʏ - {callback_query.from_user.mention}\n⬝ ꜱᴛʀᴇᴀᴍᴇᴅ ʙʏ - ɴᴏᴀʜ ᴍᴜꜱɪᴄ")

    except Exception as e:
        print(f"Error: {e}")
        callback_query.message.reply_text("An error occurred while processing your request.")
