from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID, LOGS_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<u><b>{app.mention} ꜱᴛʀᴇᴀᴍ ʟᴏɢ</b></u>

⬝ <b>ǫᴜᴇʀʏ :-</b> {message.text.split(None, 1)[1]}

↝<b>ᴇᴠᴇɴ ᴀᴛ⥮</b>
⬝<b>ᴄʜᴀᴛ ɪᴅ :-</b> <code>{message.chat.id}</code>
⬝<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :-</b> {message.chat.title}
⬝<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :-</b> @{message.chat.username}

↝<b>ǫᴜᴇʀʏ ʙʏ⥮</b>
⬝ <b>ᴜsᴇʀ ɪᴅ :-</b> <code>{message.from_user.id}</code>
⬝ <b>ɴᴀᴍᴇ :-</b> {message.from_user.mention}
⬝ <b>ᴜsᴇʀɴᴀᴍᴇ :-</b> @{message.from_user.username}

↝<b>ᴛʏᴘᴇ⥮</b> 
⬝ <b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :-</b> {streamtype}"""
        if message.chat.id != LOGS_ID:
            try:
                await app.send_message(
                    chat_id=LOGS_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
