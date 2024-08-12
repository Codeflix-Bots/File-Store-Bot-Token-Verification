from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import *

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>subaru</a>\n» ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix>subaru</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 {query.from_user.username}\n\n🎖️ Available Plans :\n\n● {PRICE1} rs For 7 Days Prime Membership\n\n● {PRICE2} rs For 1 Month Prime Membership\n\n● {PRICE3} rs For 3 Months Prime Membership\n\n● {PRICE4} rs For 6 Months Prime Membership\n\n● {PRICE5} rs For 1 Year Prime Membership\n\n\n💵 UPI ID -  {UPI_ID}\n\n(Tap to copy UPI Id)\n\n\n📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n• <u>ғɪʀsᴛ sᴛᴇᴘ</u> : ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴘʟᴀɴ ᴛᴏ ᴛʜɪs <code>rohit162@fam</code> ᴜᴘɪ ɪᴅ.\n • <u>secoɴᴅ sᴛᴇᴘ</u> : ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ᴅɪʀᴇᴄᴛʟʏ ʜᴇʀᴇ: @sewxiy \n• <u>ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴛᴇᴘ</u> : ᴏʀ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ the /bought ᴄᴏᴍᴍᴀɴᴅ.\n\nYᴏᴜʀ <ul>ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ</ul> ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀғᴛᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("• sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴀsʜᴏᴛ •", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data = "close")
                    ]
                ]
            )
