import config
import discord
import personalcommands
import usercommands


client = discord.Client()

cmd_dict = {
            "juan": usercommands.juan
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
async def on_ready():
    print('FurretBot started')


client.run(config.token)
