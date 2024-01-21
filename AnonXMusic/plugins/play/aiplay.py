from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic.core.call import Anony
from AnonXMusic import spotify, app
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_PLAYLISTS = {
    'English': 'english_playlist_id',
    'Hindi': 'hindi_playlist_id',
    'OtherLanguages': 'other_languages_playlist_id'
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
        msg.reply_text("Select a playlist:", reply_markup=InlineKeyboardMarkup(buttons))

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
        callback_query.message.reply_text(f"Playing song from {playlist_name} playlist")

    except Exception as e:
        print(f"Error: {e}")
        callback_query.message.reply_text("An error occurred while processing your request.")

if __name__ == "__main__":
    pytgcalls.run()
