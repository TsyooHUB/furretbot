import config
import datetime
import discord
import os
import pyscreenshot

client = discord.Client()


async def shutdown(message):
    await message.channel.send("Ok, shutting down. Good bye.")
    os.system('shutdown -s -t 0')


async def turnoff(message):
    await message.channel.send("Ok, turning myself off. Bye!")
    exit()


async def restart(message):
    await message.channel.send("Ok, restarting. Be right back!")
    os.system("shutdown -t 0 -r -f")


async def screenshot(message):
    await message.channel.send("Ok, sending you a screenshot.")
    img = pyscreenshot.grab()
    img_name = "screenshots/" + str(datetime.datetime.now()).replace(":", "") + ".png"
    img.save(img_name)
    await message.channel.send(file=discord.File(img_name))

cmd_dict = {
            "shut down": shutdown,
            "turn off": turnoff,
            "restart": restart,
            "screen": screenshot
            }


@client.event
async def on_message(message):
    if message.author is client.user or str(message.author.id) != config.userid:
        return False
    if type(message.channel) == discord.TextChannel:
        if client.user not in message.mentions:
            return False
    for cmd_name in cmd_dict:
        if cmd_name in message.content.lower():
            await cmd_dict[cmd_name](message)


@client.event
async def on_ready():
    print('FurretBot started')


client.run(config.token)
