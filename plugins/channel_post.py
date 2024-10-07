import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats','auth','unauth','auth_users']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"

    string = f"get-{converted_id}"
    string = string.replace("get-", "premium-")
    base64_string = await encode(string)
    link1 = f"https://telegram.me/{client.username}?start={base64_string}"

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("• ғʀᴇᴇ ʟɪɴᴋ", url=link)],
            [InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ ʟɪɴᴋ •", url=link1)]
        ]
    )

    await reply_text.edit(
        "<b>> Your Links</b>",
        disable_web_page_preview=True,
        reply_markup=keyboard
    )
