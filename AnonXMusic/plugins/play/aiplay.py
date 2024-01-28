import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic.core.call import Anony
from AnonXMusic import LOGGER, app

# Dictionary containing YouTube links for Hindi and English songs
song_links = {
    "Hindi": "",
    "English": "",
}

# Handle /aiplay command
@app.on_message(filters.command("aiplay"))
async def aiplay(_, msg):
    try:
        chat_id = msg.chat.id

        # Create buttons for Hindi and English
        buttons = [
            [InlineKeyboardButton("Hindi", callback_data="hindi"),
             InlineKeyboardButton("English", callback_data="english")]
        ]

        # Send the buttons to the user
        await msg.reply_text("Choose language:", reply_markup=InlineKeyboardMarkup(buttons))

    except Exception as e:
        LOGGER("AnonXMusic").error(f"Error in aiplay command: {e}")
        await msg.reply_text("An error occurred while processing your request.")

# Handle button clicks
@app.on_callback_query()
async def button_callback(_, callback_query):
    try:
        chat_id = callback_query.message.chat.id
        user_id = callback_query.from_user.id

        # Get the selected language
        selected_language = callback_query.data.lower()

        # Get the YouTube link based on the selected language
        youtube_link = song_links.get(selected_language)

        if not youtube_link:
            raise ValueError(f"Invalid language: {selected_language}")

        # Start playing the song on the voice chat
        Anony.join_group_call(chat_id, youtube_link, user_id=user_id)
        await callback_query.message.reply_text(f"AI Player started - Now playing {selected_language} song")

    except Exception as e:
        LOGGER("AnonXMusic").error(f"Error in button callback: {e}")
        await callback_query.message.reply_text("An error occurred while processing your request."
