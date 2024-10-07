import asyncio
import logging
import os
import random
import string
import time
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid

from bot import Bot
from config import *
from helper_func import *
from database.database import *
from database.db_premium import *

@Bot.on_message(filters.private & filters.command('auth') & filters.user(ADMINS))
async def add_premium_user(client: Client, msg: Message):
    if len(msg.command) != 3:
        await msg.reply_text("usage: /auth user_id time_limit_months")
        return
    try:
        user_id = int(msg.command[1])
        time_limit_months = int(msg.command[2])
        await add_premium(user_id, time_limit_months)
        await msg.reply_text(f"User {user_id} added as a paid user with {time_limit_months}-days plan.")
        await client.send_message(
                chat_id= user_id,
                text=f"**ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs ɴᴏᴡ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ {time_limit_months} ᴅᴀʏs sᴜʙsᴄʀɪᴘᴛɪᴏɴ**",
                parse_mode=ParseMode.MARKDOWN
            )
    except ValueError:
        await msg.reply_text("Invalid user_id or time_limit. Please recheck.")

@Bot.on_message(filters.private & filters.command('unauth') & filters.user(ADMINS))
async def pre_remove_user(client: Client, msg: Message):
    if len(msg.command) != 2:
        await msg.reply_text("useage: /unauth user_id ")
        return
    try:
        user_id = int(msg.command[1])
        await remove_premium(user_id)
        await msg.reply_text(f"User {user_id} has been removed.")
    except ValueError:
        await msg.reply_text("user_id must be an integer or not available in database.")

@Bot.on_message(filters.private & filters.command('auth_users') & filters.user(ADMINS))
async def list_premium_users_command(client, message):
    premium_users = collection.find({})
    premium_user_list = ['Premium Users in database:']

    for user in premium_users:
        user_ids = user["user_id"]
        try:
            user_info = await client.get_users(user_ids)
            username = user_info.username
            first_name = user_info.first_name
            expiration_timestamp = user["expiration_timestamp"]
            xt = (expiration_timestamp - time.time())
            x = round(xt / (24 * 60 * 60))
            premium_user_list.append(f"UserID- <code>{user_ids}</code>\nUser- @{username}\nName- <code>{first_name}</code>\nExpiry- {x} days")
        except PeerIdInvalid:
            premium_user_list.append(f"UserID- <code>{user_ids}</code>\nUser- <code>Invalid ID</code>\nName- <code>Unknown</code>\nExpiry- <code>N/A</code>")
        except Exception as e:
            premium_user_list.append(f"UserID- <code>{user_ids}</code>\nUser- <code>Error: {str(e)}</code>\nName- <code>Unknown</code>\nExpiry- <code>N/A</code>")

    if premium_user_list:
        formatted_list = [f"{user}" for user in premium_user_list]
        await message.reply_text("\n\n".join(formatted_list))
    else:
        await message.reply_text("I found 0 premium users in my DB")
