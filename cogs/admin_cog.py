import db_manager

from discord.ext import commands


class Admin(commands.cog):
    @commands.command
    async def create_tables(self, ctx):
        db_manager.db.create_tables(db_manager.User)
        await ctx.send("Tables created.")

    @commands.command
    async def drop_tables(self, ctx):
        db_manager.db.drop_tables(db_manager.User)
        await ctx.send("Tables dropped")


def setup(bot):
    bot.add_cog(Admin(bot))
