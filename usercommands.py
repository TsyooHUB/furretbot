import aiohttp
import discord
import io

from imagehandler import juan_processing


async def juan(message, command):
    async with aiohttp.ClientSession() as session:
        async with session.get(command[1]) as resp:
            buffer = io.BytesIO(await resp.read())
    await message.channel.send(file=discord.File(fp=juan_processing(buffer), filename="image.png"))
