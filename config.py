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
    START_TXT = """<b><i>Hello</i> {} 👋</b>

<b><i>This is a powerful rename bot with muti advance features -</i></b>

<b><i>• Rename Files
• Convert Videos ⇄ Files
• Custom Thumbnail and Caption</i></b>

<b><i>Bot Is Made By <a href='https://t.me/MyselfNeon'>NeonAnurag</a></i></b>"""

    ABOUT_TXT = """
╭───────────────⍟
├<b><i>🤖 My Name</i></b> : <b>{}</b>
├<b><i>🖥️ Developer</i></b> : <a href=https://t.me/OnionXbot><b><i>Contact Me</i></b></a> 
├<b><i>👨‍💻 Programer</i></b> : <a href=https://t.me/MyselfNeon><b><i>MyselfNeon</i></b></a>
├<b><i>📕 Library</i></b> : <a href=https://github.com/pyrogram><b><i>Pyrogram</i></b></a>
├<b><i>✏️ Language</i></b> : <a href=https://www.python.org><b><i>Python 3</i></b></a>
├<b><i>💾 Database</i></b> : <a href=https://cloud.mongodb.com><b><i>Mongo DB</i></b></a>
├<b><i>📢 Channel</i></b> : <a href=https://t.me/NeonFiles><b><i>Rename v4.5.0</i></a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
⁉️ <b><u>How To Set Thumbnail</u></b>
  
➪ /start - <b><i>Start The Bot And Send Any Photo To Automatically Set Thumbnail.</i></b>
➪ /del_thumb - <b><i>Use This Command To Delete Your Old Thumbnail.</i></b>
➪ /view_thumb - <b><i>Use This Command To View Your Current Thumbnail.</i></b>

⁉️ <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - <b><i>Use This Command To Set A Custom Caption</i></b>
➪ /see_caption - <b><i>Use This Command To View Your Custom Caption</i></b>
➪ /del_caption - <b><i>Use This Command To Delete Your Custom Caption</i></b>

➪ <b><i><u>Example</i></u></b> - 
<code>/set_caption 
📕 <b><i>Name</i></b> ➠ : {filename}

<b>🔗 <i>Size</i></b> ➠ : {filesize} 
<b>⏰ <i>Duration</i></b> ➠ : {duration}</code>

⁉️ <b><u>How To Rename A File</u></b>

<b><i>➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].</i></b>         

<b><i>Any Other help Contact</b></i> :- <a href=https://t.me/OnionXbot><b><i>Developer</i></b></a>
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


<b><i>💬 For Any Help Contact @OnionXbot </i></b>
"""



