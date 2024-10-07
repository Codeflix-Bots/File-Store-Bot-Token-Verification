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

# Enable logging
logging.basicConfig(level=logging.INFO)

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    logging.info(f"Received /start command from user ID: {id}")

    if not await present_user(id):
        try:
            await add_user(id)
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            return

    text = message.text
    verify_status = await get_verify_status(id)
    is_premium = await is_premium_user(id)

    logging.info(f"Verify status: {verify_status}")
    logging.info(f"Is premium: {is_premium}")

    # Check for base64 string in the command
    base64_string = text.split(" ", 1)[1] if " " in text else None

    if base64_string:
        decoded_string = await decode(base64_string)

        verify_status = await get_verify_status(id)
        if verify_status['is_verified'] and VERIFY_EXPIRE < (time.time() - verify_status['verified_time']):
            await update_verify_status(id, is_verified=False)

        if "verify_" in text:
            _, token = text.split("_", 1)
            if verify_status['verify_token'] != token:
                return await message.reply("Your token is invalid or expired. Try again by clicking /start")
            await update_verify_status(id, is_verified=True, verified_time=time.time())
            await message.reply("Your token has been successfully verified and is valid for 24 hours.", reply_markup=None, protect_content=False, quote=True)

        elif decoded_string.startswith("premium"):
            if not is_premium:
                await message.reply("Buy premium to access this content.\nTo Buy Contact @sewxiy")
                return
            
            argument = decoded_string.split("-")
            ids = []

            try:
                if len(argument) == 3:
                    start = int(argument[1])
                    end = int(argument[2])
                    ids = range(start, end + 1) if start <= end else range(start, end - 1, -1)
                elif len(argument) == 2:
                    ids = [int(argument[1])]
            except (ValueError, IndexError):
                return

            temp_msg = await message.reply("Wait A Second...")
            try:
                messages = await get_messages(client, ids)
            except Exception as e:
                await message.reply_text("Something went wrong: " + str(e)) 
                return

            await temp_msg.delete()
            for msg in messages:
                caption = CUSTOM_CAPTION.format(previouscaption=msg.caption.html if msg.caption else "", filename=msg.document.file_name) if CUSTOM_CAPTION else msg.caption.html if msg.caption else ""

                reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None

                try:
                    snt_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                    await asyncio.sleep(0.5)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    snt_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)

        elif decoded_string.startswith("get"):
            if not is_premium and not verify_status['is_verified']:
                token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                await update_verify_status(id, verify_token=token, link="")
                link = await get_shortlink(SHORTLINK_URL, SHORTLINK_API, f'https://telegram.dog/{client.username}?start=verify_{token}')
                btn = [
                    [InlineKeyboardButton("• ᴏᴘᴇɴ ʟɪɴᴋ", url=link)],
                    [InlineKeyboardButton('ᴛᴜᴛᴏʀɪᴀʟ •', url=TUT_VID)],
                ],
                [
                    InlineKeyboardButton(text="• ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ •", callback_data="premium")
                ]
            ]
                await message.reply(f"Your ads token is expired or invalid. Please verify to access the files.\n\nToken Timeout: {get_exp_time(VERIFY_EXPIRE)}\n\nThis is an ads token. If you pass 1 ad, you can use the bot for 24 hours after passing the ad.", reply_markup=InlineKeyboardMarkup(btn), protect_content=False, quote=True)
                return

            argument = decoded_string.split("-")
            ids = []

            try:
                if len(argument) == 3:
                    start = int(argument[1])
                    end = int(argument[2])
                    ids = range(start, end + 1) if start <= end else range(start, end - 1, -1)
                elif len(argument) == 2:
                    ids = [int(argument[1])]
            except (ValueError, IndexError):
                return

            temp_msg = await message.reply("Please wait...")
            try:
                messages = await get_messages(client, ids)
            except Exception as e:
                await message.reply_text("Something went wrong: " + str(e)) 
                return

            await temp_msg.delete()
            for msg in messages:
                caption = CUSTOM_CAPTION.format(previouscaption=msg.caption.html if msg.caption else "", filename=msg.document.file_name) if CUSTOM_CAPTION else msg.caption.html if msg.caption else ""

                reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None

                try:
                    snt_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                    await asyncio.sleep(0.5)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    snt_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)

    else:
        try:
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("• ғᴏʀ ᴍᴏʀᴇ •", url='https://t.me/OtakuFlix_Network/4630')],
                [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data='close'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')]
           ])
            await message.reply_text(
                text=START_MSG.format(
                    first=message.from_user.first_name,
                    last=message.from_user.last_name or "",
                    username=f'@{message.from_user.username}' if message.from_user.username else '',
                    mention=message.from_user.mention,
                    id=message.from_user.id
                ),
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                quote=True
            )
        except Exception as e:
            logging.error(f"Error in sending start message: {e}")

#=====================================================================================##

WAIT_MSG = "<b>Processing ...</b>"

REPLY_ERROR = "<code>Use this command as a reply to any telegram message without any spaces.</code>"

#=====================================================================================##

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink2),
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text='ᴛʀʏ ᴀɢᴀɪɴ',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name or "",
            username=f'@{message.from_user.username}' if message.from_user.username else '',
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot.")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except FloodWait as e:
                unsuccessful += 1
                await asyncio.sleep(e.x)
            except Exception as e:
                unsuccessful += 1
                logging.error(f"Error broadcasting message to {chat_id}: {e}")

            total += 1
            await asyncio.sleep(0.3)

        await pls_wait.delete()
        await message.reply(f"Broadcast completed!\nTotal: {total}\nSuccessful: {successful}\nBlocked: {blocked}\nDeleted: {deleted}\nUnsuccessful: {unsuccessful}")
    else:
        await message.reply(REPLY_ERROR)


