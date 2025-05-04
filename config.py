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
    START_TXT = """<b><i>Hello</i></b> {} 👋

<b><i>This is a powerful rename bot with muti advance features -</i></b>

<b><i>• Rename Files
• Convert Videos ⇄ Files
• Custom Thumbnail and Caption</i></b>

<b><i>Bot Is Made By <a href='https://t.me/MyselfNeon'>NeonAnurag</a></i></b>"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : <b>{}</b>
├<b>🖥️ Developer</b> : <a href=https://t.me/OnionXbot><b>Contact Me</b></a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/MyselfNeon><b>MyselfNeon</b></a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram><b>Pyrogram</b></a>
├<b>✏️ Language</b> : <a href=https://www.python.org><b>Python 3</b></a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com><b>Mongo DB</b></a>
├<b>📢 Channel</b> : <a href=https://t.me/NeonFiles><b>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u><i>How To Set Thumbnail</i></u></b>
  
➪ /start - <b><i>Start The Bot And Send Any Photo To Automatically Set Thumbnail.</i></b>
➪ /del_thumb - <b><i>Use This Command To Delete Your Old Thumbnail.</i></b>
➪ /view_thumb - <b><i>Use This Command To View Your Current Thumbnail.</i></b>

📑 <b><u><i>How To Set Custom Caption</i></u></b>

➪ /set_caption - <b><i>Use This Command To Set A Custom Caption</i></b>
➪ /see_caption - <b><i>Use This Command To View Your Custom Caption</i></b>
➪ /del_caption - <b><i>Use This Command To Delete Your Custom Caption</i></b>
➪ <b>Example</b> - <code>/set_caption 📕 <b><i>Name</i></b> ➠ : {filename}

<b>🔗 <i>Size</i></b> ➠ : {filesize} 

<b>⏰ <i>Duration</i></b> ➠ : {duration}</code>

✏️ <b><u><i>How To Rename A File</i></u></b>

<b><i>➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].</i></b>         

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/OnionXbot><i>Developer</i></a>
"""

    PROGRESS_BAR = """\n
 <b><i>🔗 Size :</i></b> {1} | {2}
️ <b><i>⏳️ Done :</i></b> {0}%
 <b><i>🚀 Speed :</i></b> {3}/s
️ <b><i>⏰️ ETA :</i></b> {4}
"""

    DONATE_TXT = """
<b><i>Thanks For Showing Interest In Donation! ❤️</i></b>

<b><i>If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.</i></b>

<b><i>🛍 UPI ID:</i></b> `NeonAn23@axl`
"""


    SEND_METADATA = """<b><u><i>🖼️ HOW TO SET CUSTOM METADATA</i></u></b>

For Example :-

<code>By :- <b>@NeonFiles🌷</b></code>

💬 <b><i>For Any Help Contact @OnionXbot</i></b>
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
