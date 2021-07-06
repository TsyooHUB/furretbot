import aiohttp
import discord
import io

from discord.ext import commands
from imagehandler import juan_processing


class Phil(commands.Cog):
    @commands.command()
    async def juan(self, ctx):
        img_link = ctx.message.context.split()[2]
        async with aiohttp.ClientSession() as session:
            async with session.get(img_link) as resp:
                buffer = io.BytesIO(await resp.read())
        await ctx.send(
            file=discord.File(fp=juan_processing(buffer), filename="image.png")
        )


def setup(bot):
    bot.add_cog(Phil(bot))
