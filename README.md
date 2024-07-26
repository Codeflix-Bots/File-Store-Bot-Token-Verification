# File-sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

### Changelogs
1. Ping command changed.
2. restart command added.

### Features
- Fully customisable.
- Customisable welcome
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup
- Add the bot to Database Channel with all permission

### Installation
#### Deploy on Heroku
**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Check This Tutorial Video on YouTube for any Help**<br>
**Thanks to [Erich](https://t.me/ErichDaniken) and his [InFoTel](https://t.me/InFoTel_Group) for this Video**

#### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

#### Deploy on Koyeb

The fastest way to deploy the application is to click the **Deploy to Koyeb** button below.


[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Sachinanand99/File-Sharing-Telegram-bot&branch=main&name=FileStoreBot)


#### Deploy in your VPS
````bash
git clone https://github.com/Sachinanand99/File-Sharing-Bot.git
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
#if you are using any hosting services use dotenvtemplate.txt for putting environment variables
python3 main.py
````

## Basic Commands
- `/start` - Check whether bot is online 🟢
- `/ping` - For checking ping of the bot 🔥
- `/stats` - Uptime of the bot (admin only) ⏱️
- `/users` - Total users active (admin only) 👥
- `/batch` - To generate the link in batch (admin only) 🔗
- `/genlink` - To generate link (admin only) 🔀
- `/auth` - For using the bot which will send the ID to the owner's DM. The owner will add the admin to config file and restart the bot.
- `/add_prem` - adding user to premium services(admins only)
- `/restart` - For restarting the bot(admins only)
- `/admins` - list all admins(admins only)
- `/add_admin` - For adding new admins(owner only) restart recommended
- `/del_admin` - For removing admins(owner only) restart recommended

## Secret Commands
- `/broadcast` - Reply to any message to broadcast it to all users(owner only).

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `DATABASE_NAME` Your mongo db session name
* `TIME` Time in seconds for message to get delete after downloading file
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL2` Optional: ForceSub Channel ID, leave 0 if you want disable force sub 2, bot may become a bit slower if you add this.
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding


### Token verification variables

* `USE_SHORTLINK` Turn this feature on or off using True or False
* `SHORTLINK_API_URL` Your Shortner url  api.shareus.io, 
* `SHORTLINK_API_KEY` shortner api key.
* `VERIFY_EXPIRE` verify expire time in seconds.
* `TUT_VID` Verification tutorial video link. eg: https://t.me/How_to_Download_7x/32


## Premium Verification variable
* `USE_PAYMENT` Turn this feature on or off using True of False
* `UPI_ID` Enter your UPI id
* `UPI_IMAGE_URL` Enter your UPI QR
* `SCREENSHOT_URL` Enter your profile link for verification of the users
* `PRICE1` 7 days price
* `PRICE2` 1 month price
* `PRICE3` 3 month price
* `PRICE4` 6 month price
* `PRICE5` 1 year price

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime

### Required Environment Variables
* TG_BOT_TOKEN
* APP_ID
* API_HASH
* DB_URL
* CHANNEL_LINK
* CHANNEL_ID
* OWNER_ID
* OWNER_TAG

Report Bugs, Give Feature Requests at https://github.com/Sachinanand99/File-Sharing-Telegram-bot/issues 

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Thanks to everyone who is on this awesome opensource project.

##

   **Star this Repo if you Liked it ⭐⭐⭐**

