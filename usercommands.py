import aiohttp
import discord
import io
import random
import userdetails

from imagehandler import juan_processing


async def juan(message, command):
    async with aiohttp.ClientSession() as session:
        async with session.get(command[1]) as resp:
            buffer = io.BytesIO(await resp.read())
    await message.channel.send(file=discord.File(fp=juan_processing(buffer), filename="image.png"))


async def balance(message, command):
    await message.channel.send(f"{message.author.mention} , your philcoin balance is "
                               f"{userdetails.get_philcoin_balance(message.author.id, message.author.name)}.")


async def gamble(message, command):
    reply = message.author.mention
    curr_balance = userdetails.get_philcoin_balance(message.author.id, message.author.name)
    try:
        gamble_amt = int(command[1])
        if gamble_amt > curr_balance:
            reply += " You don't have enough philcoins to play."
        elif gamble_amt <= 0:
            reply += " You can't play with that amount of philcoins."
        else:
            if random.randint(0, 1) == 0:
                rng = -1
                reply += f" Sorry, you lose! You lost {gamble_amt} philcoins."
            else:
                rng = 1
                reply += f" You won! You gained {gamble_amt} philcoins."
            userdetails.add_philcoin(message.author.id, rng * gamble_amt)
    except IndexError:
        reply += " Incorrect usage of gamble command."
    await message.channel.send(reply)
