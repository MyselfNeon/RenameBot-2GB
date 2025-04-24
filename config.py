import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","MyselfNeon")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/RQS.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '841851780').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "NeonFiles") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001889915480"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hello</b> {} 👋

<b>This is a powerful rename bot with muti advance features -</b>

<b>• Rename Files
• Convert Videos ⇄ Files
• Custom Thumbnail and Caption</b>

<b>Bot Is Made By <a href='https://t.me/MyselfNeon'>NeonAnurag</a></b>"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/OnionXbot><b>NeonAn❤️</b></a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/NeonFiles><b>MyselfNeon</b></a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram><b>Pyrogram</b></a>
├<b>✏️ Language</b> : <a href=https://www.python.org><b>Python 3</b></a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com><b>Mongo DB</b></a>
├<b>📢 Instagram</b> : <a href=https://instagram.com/neon.an_><b>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - <b>Start The Bot And Send Any Photo To Automatically Set Thumbnail.</b>
➪ /del_thumb - <b>Use This Command To Delete Your Old Thumbnail.</b>
➪ /view_thumb - <b>Use This Command To View Your Current Thumbnail.</b>

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - <b>Use This Command To Set A Custom Caption</b>
➪ /see_caption - <b>Use This Command To View Your Custom Caption</b>
➪ /del_caption - <b>Use This Command To Delete Your Custom Caption</b>
➪ <b>Example</b> - <code>/set_caption 📕 <b>Name</b> ➠ : {filename}

<b>🔗 Size</b> ➠ : {filesize} 

<b>⏰ Duration</b> ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

<b>➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].</b>         

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/OnionXbot>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

<b>If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.</b>

<b>🛍 UPI ID:</b> `NeonAn23@axl`
"""


    SEND_METADATA = """<b><u>🖼️ HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- <b>@NeonFiles🌷</b></code>

💬 For Any Help Contact @OnionXbot
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
