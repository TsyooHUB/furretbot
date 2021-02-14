from random_word import RandomWords

import config
import db_manager
import discord
import os
import pet
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


async def create(message):
    pet_name = message.content.split()[-1]
    response = "Gave "
    for user in message.mentions:
        pet.create_pet(user.id, pet_name)
        response += user.mention + " "
    await message.channel.send(f"{response} {pet_name} phil.")
    