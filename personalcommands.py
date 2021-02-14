from random_word import RandomWords

import config
import discord
import os
import db_manager
import userdetails


async def create_tables(message):
    db_manager.db.create_tables([db_manager.Register, db_manager.Pet])
    await message.channel.send("Tables created.")


async def drop_tables(message):
    db_manager.db.drop_tables([db_manager.Register, db_manager.Pet])
    await message.channel.send("Tables dropped")


async def give_philcoin(message):
    amount = message.content.split()[-1]
    response = "Gave "
    for user in message.mentions:
        userdetails.add_philcoin(user.id, user.name, amount)
        response += user.mention + " "
    await message.channel.send(f"{response} {amount} philcoins.")
