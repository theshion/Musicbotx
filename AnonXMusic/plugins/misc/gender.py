import random, requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app

BUTTON = [[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/Noah_Musicbot?startgroup=true")]]
HOT_ANIMATION = "https://telegra.ph/file/5cd8d8e3865dd8480b8c4.mp4"
CUTE_ANIMATION = "https://telegra.ph/file/2c978d637558612fcd4b9.mp4"
COCK_ANIMATION = "https://telegra.ph/file/423414459345bf18310f5.gif"
LESBIAN_ANIMATION = "https://telegra.ph/file/ea84101b261df52c2b7ac.mp4"
BOOBS_ANIMATION = "https://telegra.ph/file/60ab18e0b717b28d3c6f7.mp4"
GAY_ANIMATION = "https://telegra.ph/file/fa7953ab5e09d5f9c0b2e.mp4"
BAT_ANIMATION = "https://telegra.ph/file/b0dc1355bcd9561a91cb0.mp4"
SIG_ANIMATION = "https://telegra.ph/file/eb074c573af978d5e5d4c.mp4"
PSYCHO_ANIMATION = "https://telegra.ph/file/99bf48dc284465b820cc9.mp4"
CHAD_ANIMATION = "https://telegra.ph/file/e7598cfbc0cc088f609fb.mp4" 

@app.on_message(filters.command("wish"))
async def wish(_, message):
    if len(message.command) < 2:
        await message.reply("𝚆ʀɪᴛᴇ ʏᴏᴜʀ ᴡɪꜱʜ\n ᴇxᴀᴘᴍʟᴇ :- `/wish i become world's president´")
        return

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = message.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish =  f"""
    🍂<b>ʜᴇʏ {message.from_user.first_name}\n✨ ʏᴏᴜʀ ᴡɪꜱʜ {text}\n🍀 ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ {wish_count}%</b>
    """

    await app.send_animation(message.chat.id, animation=url, caption=wish, reply_markup=InlineKeyboardMarkup(BUTTON))



@app.on_message(filters.command(["mystats"]))
async def how_all(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"

        lullas = [
            ("horny", "ʜᴏʀɴʏ"),
            ("gay", "ɢᴀʏɴᴇꜱꜱ"),
            ("lesbian", "ʟᴇꜱʙɪᴀɴ"),
            ("boobs", "ʙᴏ*ʙᴇ ꜱɪᴢᴇ"),
            ("cock", "ᴄᴏ*ᴋ ꜱɪᴢᴇ"),
            ("cute", "ᴄᴜᴛᴇɴᴇꜱꜱ")
        ]

        result = "\n".join([f"**{lulla[1]}:** {random.randint(1, 100)}%" for lulla in lullas])
        await app.send_message(message.chat.id, text=f"📊 {mention}'ꜱ ᴏᴠᴇʀ-ᴀʟʟ ꜱᴛᴀᴛꜱ:\n{result}", reply_markup=InlineKeyboardMarkup(BUTTON))

    if message.reply_to_message:
        replied = message.reply_to_message
        user_id = replied.from_user.id
        user_name = replied.from_user.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"

        lullas = [
            ("horny", "ʜᴏʀɴʏ"),
            ("gay", "ɢᴀʏɴᴇꜱꜱ"),
            ("lesbian", "ʟᴇꜱʙɪᴀɴ"),
            ("boobs", "ʙᴏ*ʙᴇ ꜱɪᴢᴇ"),
            ("cock", "ᴄᴏ*ᴋ ꜱɪᴢᴇ"),
            ("cute", "ᴄᴜᴛᴇɴᴇꜱꜱ")
        ]

        result = "\n".join([f"**{lulla[1]}:** {random.randint(1, 100)}%" for lulla in lullas])
        await app.send_message(message.chat.id, text=f"📊 {mention}'ꜱ ᴏᴠᴇʀ-ᴀʟʟ ꜱᴛᴀᴛᴇ:\n{result}", reply_markup=InlineKeyboardMarkup(BUTTON))


@app.on_message(filters.command("horny"))
async def horny(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNY = f"🔥 <b>{mention} ɪꜱ {mm}% ʜᴏʀɴʏ.</b>"
    await app.send_animation(message.chat.id, animation=HOT_ANIMATION, caption=HORNY, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_message(filters.command("gay"))
async def gay(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"🏳‍🌈 <b>{mention} ɪꜱ {mm}% ɢᴀʏ.</b>"
    await app.send_animation(message.chat.id, animation=GAY_ANIMATION, caption=GAY, reply_markup=InlineKeyboardMarkup(BUTTON))

    
    
@app.on_message(filters.command("lesbian"))
async def lezbian(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    LESBIAN = f"🏳‍🌈 <b>{mention} ɪꜱ {mm}% ʟᴇꜱʙɪᴀɴ.</b>"
    await app.send_animation(message.chat.id, animation=LESBIAN_ANIMATION, caption=LESBIAN, reply_markup=InlineKeyboardMarkup(BUTTON))
   
    
@app.on_message(filters.command(["boob", "boobs"]))
async def boob(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"🍒 <b>{mention}'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪꜱ {mm}.</b>"
    await app.send_animation(message.chat.id, animation=BOOBS_ANIMATION, caption=BOOBS, reply_markup=InlineKeyboardMarkup(BUTTON))

    
@app.on_message(filters.command(["cock", "dick"]))
async def cock(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"🍆 <b>{mention}'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪꜱ {mm}ᴄᴍ.</b>"
    await app.send_animation(message.chat.id, animation=COCK_ANIMATION, caption=COCK, reply_markup=InlineKeyboardMarkup(BUTTON))

    
    
@app.on_message(filters.command("cute"))
async def cute(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"✨ <b>{mention} {mm}% ᴄᴜᴛᴇ.</b>"
    await app.send_animation(message.chat.id, animation=CUTE_ANIMATION, caption=CUTE, reply_markup=InlineKeyboardMarkup(BUTTON))

    
@app.on_message(filters.command("sigma"))
async def sigma(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    SIGMA = f"🗿 <b>{mention} ɪꜱ {mm}% ꜱɪɢᴍᴀ.</b>"
    await app.send_animation(message.chat.id, animation=SIG_ANIMATION, caption=SIGMA, reply_markup=InlineKeyboardMarkup(BUTTON))


@app.on_message(filters.command("chad"))
async def chad(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CHAD = f"🗿 <b>{mention} ɪꜱ {mm}% ᴄʜᴀᴅ.</b>"
    await app.send_animation(message.chat.id, animation=CHAD_ANIMATION, caption=CHAD, reply_markup=InlineKeyboardMarkup(BUTTON))
    

@app.on_message(filters.command("batman"))
async def batman(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BATMAN = f"🦇 <b>{mention} ɪꜱ {mm}% ʙᴀᴛᴍᴀɴ.</b>"
    await app.send_animation(message.chat.id, animation=BAT_ANIMATION, caption=BATMAN, reply_markup=InlineKeyboardMarkup(BUTTON))


@app.on_message(filters.command("psycho"))
async def psycho(_, message):
    user_id = message.from_user.id
    user_name = message .from_user.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    PSYCHO = f"😈 <b>{mention} ɪꜱ {mm}% ᴘꜱʏᴄʜᴏ.</b>"
    await app.send_animation(message.chat.id, animation=PSYCHO_ANIMATION, caption=PSYCHO, reply_markup=InlineKeyboardMarkup(BUTTON))


