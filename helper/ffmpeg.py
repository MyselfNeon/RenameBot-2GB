import asyncio
import os

async def run_command(command):
    """Run shell command asynchronously and return output."""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()

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
