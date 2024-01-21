import os
from time import time
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters

from AnonXMusic import app


def calculate_time(start_time, end_time):
    elapsed_time = end_time - start_time
    return f"{elapsed_time:.2f} ꜱᴇᴄᴏɴᴅꜱ"



def text_set(text):
    lines = []
    if len(text) <= 50:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 50:
                lines.append(line)
            else:
                k = len(line) // 50
                lines.extend(line[((z - 1) * 50) : (z * 50)] for z in range(1, k + 2))
    return lines[:25]




@app.on_message(filters.command("write"))
async def handwrite(client, message):
    start_time = time()  # Record the start time
    if message.reply_to_message and message.reply_to_message.text:
        txt = message.reply_to_message.text
    elif len(message.command) > 1:
        txt = message.text.split(None, 1)[1]
    else:
        return await message.reply(
            f"ʜᴇʏᴏ {message.from_user.mention} ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ɴᴏᴛᴇ ʙᴏᴏᴋ.\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n⥤ ᴜꜱᴀɢᴇ :- <code>/write Noah</code>"
        )
    nan = await message.reply_text("ᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ ᴏɴ ɴᴏᴛᴇ-ʙᴏᴏᴋ\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nᴊᴜꜱᴛ ᴡᴀɪᴛ ꜱᴏᴍᴇ ꜱᴇᴄᴏɴᴅꜱ...")
    try:
        img = Image.open("AnonXMusic/writo.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AnonXMusic/assfont.ttf", 30)
        x, y = 165, 165
        lines = text_set(txt)
        line_height = font.getbbox("hg")[3]
        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + line_height - 0
        file = f"nulis_{message.from_user.id}.jpg"
        img.save(file)
        end_time = time()  # Record the end time after writing
        elapsed_time = calculate_time(start_time, end_time)

        if os.path.exists(file):
            await message.reply_photo(
                photo=file, caption=f"""<b>⬝ sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴇ ʏᴏᴜʀ ᴛᴇxᴛ ᴏɴ ɴᴏᴛᴇ-ʙᴏᴏᴋ.
    ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⬝ ᴡʀɪᴛᴛᴇɴ ʙʏ - {client.me.mention}
⬝ ǫᴜᴇʀʏ ʙʏ - {message.from_user.mention}
⬝ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ - {elapsed_time}</b>"""
            )
            os.remove(file)
            await nan.delete()
    except Exception as e:
        return await message.reply(e)
        
