import config
import datetime
import discord
import os
import pyscreenshot

token = config.token
userid = config.userid

client = discord.Client()


def process_message(msg):
    if msg.author is client.user:
        return None
    if type(msg.channel) == discord.TextChannel:
        if client.user in msg.mentions:
            if str(msg.author.id) != userid:
                return False
            return True
        else:
            return None
    else:
        if msg.author.id != userid:
            return False
        return True


@client.event
async def on_message(message):
    result = process_message(message)
    if result:
        content = message.content.lower()
        extra = ""
        if "hello" in content or "hey" in content or "hi" in content:
            extra += "Hey! "
        if "please" in content:
            extra += "Of course! "
        if "thanks" in content:
            extra += "No problem. "
        if extra != "":
            await message.channel.send(extra)
        if "shut down" in content:
            await message.channel.send("Ok, shutting down. Good bye.")
            os.system('shutdown -s -t 0')
        elif "turn off" in content:
            await message.channel.send("Ok, turning myself off. Bye!")
            exit()
        elif "restart" in content:
            await message.channel.send("Ok, restarting. Be right back!")
            os.system("shutdown -t 0 -r -f")
        elif "screen" in content:
            await message.channel.send("Ok, sending you a screenshot.")
            img = pyscreenshot.grab()
            img_name = "screenshots/"+str(datetime.datetime.now()).replace(":", "")+".png"
            img.save(img_name)
            await message.channel.send(file=discord.File(img_name))
        else:
            if extra == "":
                await message.channel.send("Sorry, I couldn't process that command.")
    elif result is False:
        await message.channel.send("Don't tell me what to do!")


@client.event
async def on_ready():
    print('FurretBot started')

client.run(token)
