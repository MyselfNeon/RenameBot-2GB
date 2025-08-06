import asyncio
import os
import time
from helper.progress import progress_for_pyrogram

async def run_command(command):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()


async def compress_video(input_file, output_file, message, start_time):
    command = (
        f'ffmpeg -i "{input_file}" -vcodec libx264 -crf 28 "{output_file}" -y'
    )
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    while True:
        await asyncio.sleep(5)
        if process.returncode is not None:
            break
        try:
            current_time = time.time()
            await progress_for_pyrogram(
                current_time - start_time,
                100,
                "Compressing",
                message,
                start_time
            )
        except Exception:
            pass
    return output_file


async def convert_video(input_file, output_file, message, start_time):
    command = (
        f'ffmpeg -i "{input_file}" -c:v libx264 -preset ultrafast -c:a aac "{output_file}" -y'
    )
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    while True:
        await asyncio.sleep(5)
        if process.returncode is not None:
            break
        try:
            current_time = time.time()
            await progress_for_pyrogram(
                current_time - start_time,
                100,
                "Converting",
                message,
                start_time
            )
        except Exception:
            pass
    return output_file


async def extract_audio(input_file, output_file):
    command = f'ffmpeg -i "{input_file}" -vn -acodec copy "{output_file}" -y'
    await run_command(command)
    return output_file


async def set_custom_metadata(input_file, output_file, metadata):
    """Set custom metadata title using ffmpeg."""
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file does not exist")

    import shlex
    safe_metadata = shlex.quote(metadata)

    command = f'ffmpeg -i "{input_file}" -metadata title={safe_metadata} -c copy "{output_file}" -y'
    _, stderr = await run_command(command)

    if "Error" in stderr or not os.path.exists(output_file):
        raise Exception(f"FFmpeg failed to add metadata:\n{stderr}")

    return output_file
