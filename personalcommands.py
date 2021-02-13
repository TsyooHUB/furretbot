from random_word import RandomWords

import config
import discord
import os
import userdetails


async def create_tables(message):
    userdetails.db.create_tables([userdetails.Register])
    await message.channel.send("Tables created.")


async def drop_tables(message):
    userdetails.db.drop_tables([userdetails.Register])
    await message.channel.send("Tables dropped")


async def give_philcoin(message):
    amount = message.content.split()[-1]
    response = "Gave "
    for user in message.mentions:
        if user.id != config.client_id:
            userdetails.add_philcoin(user.id, user.name, amount)
            response += user.mention + " "
    await message.channel.send(f"{response} {amount} philcoins.")


async def generate_random_word(message):
    r = RandomWords()
    await message.channel.send(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun, adj"))