from typing import Union
from datetime import datetime

from AnonXMusic.core.call import Anony
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from AnonXMusic import app
from AnonXMusic.utils import help_pannel, ahelp_pannel, bot_sys_stats
from AnonXMusic.utils.database import get_lang
from AnonXMusic.utils.decorators.language import LanguageStart, languageCB
from AnonXMusic.utils.inline.help import help_back_markup, ahelp_back_markup, private_help_panel
from AnonXMusic.utils.inline.start import exp_panel, feature_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers, ai


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["chelp_1"], reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboardb = feature_panel(_)
        keyboard = InlineKeyboardMarkup(keyboardb)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"],
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    akeyboard = ahelp_back_markup(_)
    if cb == "a2":
        await CallbackQuery.edit_message_text(ai.AF_2, reply_markup=akeyboard)
    elif cb == "a3":
        await CallbackQuery.edit_message_text(ai.AF_3, reply_markup=akeyboard)
    elif cb == "a4":
        await CallbackQuery.edit_message_text(ai.AF_4, reply_markup=akeyboard)
    elif cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)



@app.on_message(filters.command(["ahelp"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("ai_features") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = ahelp_pannel(_, True)
        await update.edit_message_text(
            _["ahelp_1"], reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboardb = feature_panel(_, True)
        keyboard = InlineKeyboardMarkup(keyboardb)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"],
            reply_markup=keyboard,
        )

@app.on_callback_query(filters.regex("ahelp_callback") & ~BANNED_USERS)
@languageCB
async def ahelper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = ahelp_back_markup(_)
    if cb == "a1":
        await CallbackQuery.edit_message_text(ai.AF_1, reply_markup=keyboard)
    elif cb == "a2":
        await CallbackQuery.edit_message_text(ai.AF_2, reply_markup=keyboard)
    elif cb == "a3":
        await CallbackQuery.edit_message_text(ai.AF_3, reply_markup=keyboard)
    elif cb == "a4":
        await CallbackQuery.edit_message_text(ai.AF_4, reply_markup=keyboard)


@app.on_callback_query(filters.regex("exp_helper") & ~BANNED_USERS)
async def exp_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard_buttons = exp_panel(_)
        keyboard_markup = InlineKeyboardMarkup(keyboard_buttons)
        await update.edit_message_text(_["exp_1"], reply_markup=keyboard_markup)
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = exp_panel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["exp_1"],
            reply_markup=keyboard,
        )


@app.on_callback_query(filters.regex("Noah_features") & ~BANNED_USERS)
async def noah_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard_buttons = feature_panel(_)
        keyboard_markup = InlineKeyboardMarkup(keyboard_buttons)
        await update.edit_message_text(_["help_1"], reply_markup=keyboard_markup)
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = feature_panel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"],
            reply_markup=keyboard,
        )


@app.on_callback_query(filters.regex("call_sys") & ~BANNED_USERS)
@languageCB
async def sys_cb(client, CallbackQuery, _):
    start = datetime.now()
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await CallbackQuery.answer(
        _["ping_6"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        show_alert=True,
    )
