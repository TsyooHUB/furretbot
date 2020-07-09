import os
import pyscreenshot
import discord
import datetime


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
    img_name = "images/screenshots/" + str(datetime.datetime.now()).replace(":", "") + ".png"
    img.save(img_name)
    await message.channel.send(file=discord.File(img_name))