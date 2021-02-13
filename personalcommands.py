import os
import discord
import userdetails


async def debug_philbank(message):
    print(userdetails.get_philbank())


async def create_tables(message):
    userdetails.db.create_tables([userdetails.Register])
    await message.channel.send("Tables created.")
