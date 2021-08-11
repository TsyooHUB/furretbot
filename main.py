import config
import os

from discord.ext import commands


bot = commands.Bot(command_prefix=config.prefix)

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
bot.run(os.environ["token"])

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}') #loads the extension in the "cogs" folder
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded "{extension}"')

    return


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}') #unloads the extension in the "cogs" folder
    await ctx.send(f'Unloaded "{extension}"')
    print(f'Unoaded "{extension}"')

    return