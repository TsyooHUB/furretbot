import discord

from discord.ext import commands
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash import cog_ext

class RPS(commands.Cog):
  buttons = [
      create_button(
        style=ButtonStyle.green,
        label="Test"
      ),
    ]
    
  action_row = create_actionrow(*buttons)
    
  @cog_ext.cog_slash()
  async def challenge(self, ctx):
    await ctx.send("Yahoo", components=[action_row])

def setup(bot):
    bot.add_cog(RPS(bot))
