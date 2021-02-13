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
            "gamble": usercommands.gamble
            }

p_cmd_dict = {
            "shut down": personalcommands.shutdown,
            "turn off": personalcommands.turnoff,
            "restart": personalcommands.restart,
            "screen": personalcommands.screenshot
            }


@client.event
async def on_message(message):
    try:
        if message.content.index(config.prefix) == 0:
            usr_cmd = message.content[1:].split()
            for cmd_name in cmd_dict:
                if cmd_name == usr_cmd[0]:
                    await cmd_dict[cmd_name](message, usr_cmd)

        if message.author is client.user or str(message.author.id) != config.userid:
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
    f not os.path.exists('data/philbank.json'):
        open('data/philbank.json', 'w')
    if os.stat("data/philbank.json").st_size != 0:
        userdetails.start_bank()
    for user in client.users:
        if not userdetails.register_exists(user.id):
            userdetails.add_register(user.id, userdetails.Register(user.name, 0))
    userdetails.save_philbank()

client.run(os.environ['token'])
