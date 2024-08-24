![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=FILE+SHARING+!;CREATED+BY+CODEFLIX+DEVELOPER!;A+ADVANCE+BOT+WITH+TOKEN+FEATURE!)
</p>


* <b>𝟸 ғsᴜʙ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/Codeflix-Bots/FileStore)</b>
* <b>ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/Codeflix-Bots/FileStore/tree/AutoDelete)</b>
* <b>𝟺 ғsᴜʙ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/Codeflix-Bots/FileStore/tree/multi-fsub)</b>

 ━━━━━━━━━━━━━━━━━
<details>
<summary><h3>
- <b> ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴠᴀʀɪᴀʙʟᴇs</b>
</h3></summary>

## Features
- Store posts and documents.
- Access content via special links.
- Easy to deploy and customize.
- Token Verifiction
- Auto Deletion

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID ` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DB_URI ` Your mongo db url 
* `DB_name ` Your mongo db session name ( random )
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/.md#custom_stats'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML

### Token Variables

* `IS_VERIFY` = Default : "True" (if you want off : False )
* `SHORTLINK_URL` = Your shortner Url ( ex. "api.shareus.io")
* `SHORTLINK_API` = Your shortner API (ex. "PUIAQBIFrydvLhIzAOeGV8yZppu")
* `VERIFY_EXPIRE` = ( ex. 86400)) # Add time in seconds



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

</details>

Report Bugs, Give Feature Requests at <b>[ᴄᴏᴅᴇғʟɪx ʙᴏᴛs](https://t.me/codeflix_bots)  ➻  [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/CodeflixSupport) </b>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<details>
<summary><h3>
- <b> ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs </b>
</h3></summary>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/Codeflix-Bots/File-Store-Bot-Token-Verification">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy On Heroku">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴋᴏʏᴇʙ 」─
</h3>
<p align="center"><a href="https://app.koyeb.com/deploy?type=git&repository=github.com/Codeflix-Bots/File-Store-Bot-Token-Verification&branch=main&name=main">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy On Koyeb">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʀᴀɪʟᴡᴀʏ 」─
</h3>
<p align="center"><a href="https://railway.app/deploy?template=https://github.com/Codeflix-Bots/File-Store-Bot-Token-Verification">
     <img height="45px" src="https://railway.app/button.svg">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʀᴇɴᴅᴇʀ 」─
</h3>
<p align="center"><a href="https://render.com/deploy?repo=https://github.com/Codeflix-Bots/File-Store-Bot-Token-Verification">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a></p>
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴠᴘs 」─
</h3>
<p>
<pre>
git clone https://github.com/Codeflix-Bots/File-Store-Bot-Token-Verification
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

<h3>「 ᴄʀᴇᴅɪᴛs 」
</h3>

- <b>[ᴄᴏᴅᴇғʟɪx ʙᴏᴛs](https://t.me/codeflix_bots)  ➻  [ʙᴀsᴇ ᴄᴏᴅᴇ](https://t.me/codeflix_bots) </b>
- <b>[sᴜʙᴀʀᴜ](https://github.com/erotixe)  ➻  [ᴇᴠᴇʀʏᴛʜɪɴɢ](https://t.me/cosmic_freak) </b>
 
<b>ᴀɴᴅ ᴀʟʟ [ᴛʜᴇ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs](https://telegram.me/codeflix-bots) ᴡʜᴏ ʜᴇʟᴩᴇᴅ ɪɴ ᴍᴀᴋɪɴɢ  ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛᴏᴋᴇɴ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴜsᴇꜰᴜʟ & ᴩᴏᴡᴇʀꜰᴜʟ 🖤 </b>

## 📌  𝑵𝒐𝒕𝒆

ᴊᴜꜱᴛ ꜰᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ ᴀɴᴅ ᴇᴅɪᴛ ᴀꜱ ᴘᴇʀ ʏᴏᴜʀ ɴᴇᴇᴅꜱ.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
