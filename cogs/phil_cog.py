import aiohttp
import discord
import io
import user_util

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

    @commands.command()
    async def balance(self, ctx):
        await ctx.send(
            f"{ctx.author.mention} , your philcoin balance is "
            f"{user_util.get_philcoin_balance(ctx.author.id, ctx.author.name)}."
        )


def setup(bot):
    bot.add_cog(Phil(bot))
