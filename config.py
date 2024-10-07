
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6966079567:AAEMZs_kK9VwPWXbZfjW6kpYq1Yv4TiRpbo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28264594"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "94ca8a089020a2290fd29a41f18acb94")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001995978690"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))

#Port
PORT = os.environ.get("PORT", "8080")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://publicdb:publicdb@cluster0.aisg0rh.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "codeflix")


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "inshorturl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "1d74269ab2c3349995cd15776033eea192df8327")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "10")) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Anime_Cruise_Netflix")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001495022147"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001723817903"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6497757690").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Codeflix_Bots</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('FALSE', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
