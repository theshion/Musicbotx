import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from AnonXMusic import app as Yumikoo
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from typing import Union, Optional
from config import OWNER_ID, BANNED_USERS

SUDO_USERS = [6116157753]

gban_db = BANNED_USERS

button = InlineKeyboardMarkup([
            [
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/NoahMusicupdates"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close_data")            
                              ]
])


# --------------------------------------------------------------------------------- #


INFO_TEXT = """
╶╴╺╸╶╴╺╸╶╴╺╸╶╴╺╸╶╴╺╸╶╴
<b>ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ⥮</b>

⬝ ᴜsᴇʀ ɪᴅ - <code>{}</code>
⬝ ɴᴀᴍᴇ - {}
⬝ ᴜsᴇʀɴᴀᴍᴇ - @{}
⬝ ᴍᴇɴᴛɪᴏɴ - {}
⬝ ʀᴇꜱᴛʀɪᴄᴛɪᴏɴ - {}
⬝ ᴠᴇʀɪꜰɪᴇᴅ - {}
⬝ ʙᴏᴛ - {}
⬝ ꜱᴛᴀᴛᴜꜱ - <code>{}</code>

⬝ ᴘʀᴇᴍɪᴜᴍ - {}

⬝ ɢʙᴀɴ - {}

⬝ ʟᴀꜱᴛ ꜱᴇᴇɴ -\n<code>{}</code>\n
⬝ ᴅᴄ ɪᴅ - {}
⬝ ʙɪᴏ - {}
╶╴╺╸╶╴╺╸╶╴╺╸╶╴╺╸╶╴╺╸╶╴
"""


# --------------------------------------------------------------------------------- #
async def usergrade(user_id):
   try:
      user = await Yumikoo.get_users(user_id)
      user_id = user.id         
      if user_id == OWNER_ID:
         return "ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ."
      elif user_id == SUDO_USERS:
         return "ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ʟɪꜱᴛᴇɴᴇʀ ʙᴜᴛ ᴀʟꜱᴏ ᴀ ꜱᴜᴘᴘᴏʀᴛᴇʀ."
      elif user_id != OWNER_ID:
         return "ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴊᴜꜱᴛ ᴀɴ ᴀᴠᴇʀᴀɢᴇ ʟɪꜱᴛᴇɴᴇʀ."
      elif user_id != SUDO_USERS:
         return "ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴊᴜꜱᴛ ᴀɴ ᴀᴠᴇʀᴀɢᴇ ʟɪꜱᴛᴇɴᴇʀ."  
      elif user_id == 6116157753:
         return "ʟᴏʟ ɪᴛ'ꜱ ᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍᴇʀ."           
   except:
        return "None"
               
    


async def userstatus(user_id):
   try:
      user = await Yumikoo.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "ᴜꜱᴇʀ ʟᴀꜱᴛ ꜱᴇᴇɴ ʀᴇᴄᴇɴᴛʟʏ."
      elif x == enums.UserStatus.LAST_WEEK:
          return "ᴜꜱᴇʀ ᴡᴀꜱ ꜱᴇᴇɴ ʟᴀꜱᴛ ᴡᴇᴇᴋ."
      elif x == enums.UserStatus.LONG_AGO:
          return "ᴜꜱᴇʀ ʟᴀꜱᴛ ꜱᴇᴇɴ ᴡᴀꜱ ʟᴏɴɢ ᴛɪᴍᴇ ᴀɢᴏ."
      elif x == enums.UserStatus.OFFLINE:
          return "ᴜꜱᴇʀ ɪꜱ ᴏꜰꜰʟɪɴᴇ."
      elif x == enums.UserStatus.ONLINE:
         return "ᴜꜱᴇʀ ɪꜱ ᴏɴʟɪɴᴇ."
   except:
        return "**^~^ ʙᴇᴇᴘ ʙᴏᴏᴘ ᴇʀʀᴏʀ.**"
    

 

@Yumikoo.on_message(filters.command(["info", "userinfo", "myinfo", "profile"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
            
    msg = await message.reply_text("**ɢᴇᴛᴛɪɴɢ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ⬖**")   
    await msg.edit_text("ɢᴇᴛᴛɪɴɢ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ⬝") 

    await msg.edit_text("ɢᴇᴛᴛɪɴɢ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ⬝⬝") 

    await msg.edit_text("ɢᴇᴛᴛɪɴɢ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ⬝⬝⬝")        

    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await Yumikoo.get_chat(user_id)
            user = await Yumikoo.get_users(user_id)
            status = await usergrade(user.id)
            last_seen = await userstatus(user.id)        
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            ai = user.is_bot   
            riyal = user.is_premium        
            gbanned_info = user.id in gban_db
            gban = gbanned_info[0] if gbanned_info else False         
            premium = user.is_verified
            restricted = user.is_restricted
            if user.photo:
                photo = await Yumikoo.download_media(user.photo.big_file_id)
            else:
                # If the user doesn't have a profile picture, use a default image
                default_photo_path = 'AnonXMusic/utils/unknown.jpg'  # Update the path accordingly
                photo = default_photo_path
        
            caption = INFO_TEXT.format(
                id, name, username, mention, restricted, premium, ai, status, riyal, gban, last_seen, dc_id, bio)

            if photo:
                await Yumikoo.send_photo(chat_id, photo=photo, caption=caption, reply_to_message_id=message.id, reply_markup=button)
            else:
                await Yumikoo.send_message(chat_id, caption, reply_to_message_id=message.id, reply_markup=button)

            await msg.delete()                
        except Exception as e:
            await message.reply_text(str(e))        
            
    elif not message.reply_to_message:
        try:
            user_info = await Yumikoo.get_chat(user_id)
            user = await Yumikoo.get_users(user_id)
            status = await usergrade(user.id)
            last_seen = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            ai = user.is_bot
            riyal = user.is_premium        
            gbanned_info = user.id in gban_db
            gban = gbanned_info[0] if gbanned_info else False
            premium = user.is_verified
            restricted = user.is_restricted        
            if user.photo:
                photo = await Yumikoo.download_media(user.photo.big_file_id)
            else:
                # If the user doesn't have a profile picture, use a default image
                default_photo_path = 'AnonXMusic/utils/unknown.jpg'  # Update the path accordingly
                photo = default_photo_path
                        
            caption = INFO_TEXT.format(
                id, name, username, mention, restricted, premium, ai, status, riyal, gban, last_seen, dc_id, bio)

            if photo:
                await Yumikoo.send_photo(chat_id, photo=photo, caption=caption, reply_to_message_id=message.id, reply_markup=button)
            else:
                await Yumikoo.send_message(chat_id, caption, reply_to_message_id=message.id, reply_markup=button)

            await msg.delete()                
        except Exception as e:
            await message.reply_text(str(e))

            
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await Yumikoo.get_chat(user_id)
            user = await Yumikoo.get_users(user_id)
            status = await usergrade(user.id)
            last_seen = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            ai = user.is_bot
            riyal = user.is_premium
            gbanned_info = user.id in gban_db
            gban = gbanned_info[0] if gbanned_info else False         
            premium = user.is_verified
            restricted = user.is_restricted 
            if user.photo:
                photo = await Yumikoo.download_media(user.photo.big_file_id)
            else:
                # If the user doesn't have a profile picture, use a default image
                default_photo_path = 'AnonXMusic/utils/unknown.jpg'  # Update the path accordingly
                photo = default_photo_path
                        
            caption = INFO_TEXT.format(
                id, name, username, mention, restricted, premium, ai, status, riyal, gban, last_seen, dc_id, bio)

            if photo:
                await Yumikoo.send_photo(chat_id, photo=photo, caption=caption, reply_to_message_id=message.id, reply_markup=button)
            else:
                await Yumikoo.send_message(chat_id, caption, reply_to_message_id=message.id, reply_markup=button)

            await msg.delete()        
        except Exception as e:
            await message.reply_text(str(e))
            
