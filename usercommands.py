import aiohttp
import discord
import io
import pet
import random
import userdetails

from imagehandler import juan_processing


async def juan(message, command):
    async with aiohttp.ClientSession() as session:
        async with session.get(command[1]) as resp:
            buffer = io.BytesIO(await resp.read())
    await message.channel.send(
        file=discord.File(fp=juan_processing(buffer), filename="image.png")
    )


async def balance(message, command):
    await message.channel.send(
        f"{message.author.mention} , your philcoin balance is "
        f"{userdetails.get_philcoin_balance(message.author.id, message.author.name)}."
    )


async def gamble(message, command):
    response = message.author.mention
    curr_balance = userdetails.get_philcoin_balance(
        message.author.id, message.author.name
    )
    try:
        gamble_amt = int(command[1])
        if gamble_amt > curr_balance:
            response += " You don't have enough philcoins to play."
        elif gamble_amt <= 0:
            response += " You can't play with that amount of philcoins."
        else:
            if random.randint(0, 1) == 0:
                rng = -1
                response += f" Sorry, you lose! You lost {gamble_amt} philcoins."
            else:
                rng = 1
                response += f" You won! You gained {gamble_amt} philcoins."
            userdetails.add_philcoin(
                message.author.id, message.author.name, rng * gamble_amt
            )
    except IndexError:
        response += " Incorrect usage of gamble command."
    await message.channel.send(response)


async def buy_pet(message, command):
    response = message.author.mention
    curr_balance = userdetails.get_philcoin_balance(
        message.author.id, message.author.name
    )
    if curr_balance < 500:
        response += "You don't have have enough philcoins to purchase a pet."
    elif pet.get_num_pets(message.author.id) >= pet.MAX_PETS:
        response += (
            f"You have too many pets, the maximum amount you can have is {pet.MAX_PETS}"
        )
    else:
        userdetails.add_philcoin(
            message.author.id, message.author.name, -1 * pet.CURRENT_PET_PRICE
        )
        response += f" You got a {pet.generate_pet(message.author.id)} phil!"
    await message.channel.send(response)


async def pets(message, command):
    await message.channel.send(message.author.mention + pet.get_pets(message.author.id))


async def pickup(message, command):
    pickup = pet.get_pickup(command[1])
    if pickup:
        userdetails.add_philcoin(message.author.id, message.author.name, pickup)
        response = f"{message.author.mention}, your {command[1]} phil got you {pickup} philcoins!"
    elif pickup is None:
        response = (
            f"Something went wrong when attempting to get your pickup from {command[1]}"
        )
    else:
        response = (
            f"You have already claimed the pickup award from {command[1]} phil today."
        )
    await message.channel.send(response)


async def fuse(message, command):
    response = message.author.mention

    pet.fuse_pets(pet.get_pet(command[1]), pet.get_pet(command[2]))
    response += f" {command[2]} phil successfully fused into {command[1]} phil."
    await message.channel.send(response)
