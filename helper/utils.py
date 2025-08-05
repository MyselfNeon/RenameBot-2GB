import math, time, re, os, shutil
from datetime import datetime
from pytz import timezone
from config import Config, Txt 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ✅ Pixel-style multi-symbol progress bar: ░▒▓█
def generate_multi_symbol_progress_bar(percentage: float, symbols: list, length: int = 20) -> str:
    if not symbols or len(symbols) < 2:
        raise ValueError("At least 2 symbols required.")
        
    total_levels = len(symbols)
    progress_per_block = 100 / length
    current_progress = percentage

    bar = ""
    for _ in range(length):
        block_percentage = min(current_progress, progress_per_block)
        symbol_index = math.floor((block_percentage / 100) * total_levels)
        symbol_index = min(symbol_index, total_levels - 1)
        bar += symbols[symbol_index]
        current_progress -= progress_per_block

    return bar


# ✅ Progress bar display function for Pyrogram bots
async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:        
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        # 🔁 New pixel-style icons
        pixel_symbols = ["█", "░"]
        progress = generate_multi_symbol_progress_bar(percentage, pixel_symbols)

        tmp = progress + Txt.PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),            
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",               
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✖️ 𝖢𝖺𝗇𝖼𝖾𝗅 ✖️", callback_data="close")]]
                )                                               
            )
        except:
            pass


# ✅ Convert bytes to human-readable format
def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


# ✅ Convert milliseconds to string time
def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]


# ✅ Convert seconds into HH:MM:SS
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


# ✅ Log new user usage
async def send_log(b, u):
    if Config.LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            Config.LOG_CHANNEL,
            f"<b><u><i>𝖭𝖾𝗐 𝖴𝗌𝖾𝗋 𝖲𝗍𝖺𝗋𝗍𝖾𝖽 𝖳𝗁𝖾 𝖡𝗈𝗍</i></u></b> \n\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖬𝖾𝗇𝗍𝗂𝗈𝗇</b> : {u.mention}\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖨𝖣</b> : `{u.id}`\n"
            f"<b>𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾</b> : {u.first_name} \n"
            f"<b>𝖫𝖺𝗌𝗍 𝖭𝖺𝗆𝖾</b> : {u.last_name} \n"
            f"<b>𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾</b> : @{u.username} \n"
            f"<b>𝖴𝗌𝖾𝗋 𝖫𝗂𝗇𝗄</b> : <a href='tg://openmessage?user_id={u.id}'>𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾</a>\n\n"
            f"<b>𝖣𝖺𝗍𝖾</b> : {date}\n"
            f"<b>𝖳𝗂𝗆𝖾</b> : {time}"
        )


# ✅ Prefix + suffix filename formatter
def add_prefix_suffix(input_string, prefix='', suffix=''):
    pattern = r'(?P<filename>.*?)(\.\w+)?$'
    match = re.search(pattern, input_string)
    if match:
        filename = match.group('filename')
        extension = match.group(2) or ''
        if prefix == None:
            if suffix == None:
                return f"{filename}{extension}"
            return f"{filename} {suffix}{extension}"
        elif suffix == None:
            if prefix == None:
                return f"{filename}{extension}"
            return f"{prefix}{filename}{extension}"
        else:
            return f"{prefix}{filename} {suffix}{extension}"
    else:
        return input_string


# ✅ Create folder or reset it
def makedir(name: str):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)