FurretBot
-----------------------------------
FurretBot is a Discord bot that utilizes discord.py and pyscreenshot to allow you to have functionality over your
computer (by using your phone or other device) while you may be away. 

Its current features are:

- Shutting down or restarting your computer
- Taking a screenshot and sending it to you 
- Turning itself off

by sending messages through Discord.

You will need to set your token and Discord user id (for the purposes of not allowing
other people to turn your computer off if it is in a public server; this is NOT your tag, you can
find it by doing something like print(message.author.id) and sending a message while the bot is running)
in the config.py file. You should also create a directory called "screenshots" in the same directory as
these files because that's the path I have to save them and I haven't added anything to create the folder
if it doesn't exist yet.

I would recommend setting it up so that it auto-launches on computer start-up. 
It can probably be cleaned up in areas like using a dict and etc but I just wanted it
to work for the time being. May merge this with another bot in the future.