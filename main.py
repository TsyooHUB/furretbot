import config
import os

from discord.ext import commands


bot = commands.Bot(command_prefix=config.prefix)

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        print(filename)
        bot.load_extension(f"cogs.{filename[:-3]}")
bot.run(os.environ["token"])