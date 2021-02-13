import os
import discord
import userdetails


async def debug_philbank(message):
    print(userdetails.philbank)
    await message.channel.send(userdetails.philbank)