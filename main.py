import config
import discord
import os
import personalcommands
import userdetails
import usercommands


client = discord.Client()


cmd_dict = {
            "juan": usercommands.juan,
            "balance": usercommands.balance,
            "gamble": usercommands.gamble,
            "buy_pet": usercommands.buy_pet
            }

p_cmd_dict = {
            "create tables": personalcommands.create_tables,
            "drop tables": personalcommands.drop_tables,
            "give philcoins": personalcommands.give_philcoin
            }


@client.event
async def on_message(message):
    try:
        if message.content.index(config.prefix) == 0:
            usr_cmd = message.content[1:].split()
            for cmd_name in cmd_dict:
                if cmd_name == usr_cmd[0]:
                    await cmd_dict[cmd_name](message, usr_cmd)

        if message.author is client.user or str(message.author.id) != os.environ['owner_id']:
            return False
        
        if type(message.channel) == discord.TextChannel:
            if client.user not in message.mentions:
                return False

        for cmd_name in p_cmd_dict:
            if cmd_name in message.content.lower():
                await p_cmd_dict[cmd_name](message)
    except ValueError:
        return False


@client.event
async def on_reaction_add(reaction, user):
    if "philcoin" in str(reaction) and reaction.message.author.id != user.id:
        userdetails.add_philcoin(reaction.message.author.id, 1)


@client.event
async def on_ready():
    print('FurretBot started')
    

client.run(os.environ['token'])
config.client_id = client.user.id
