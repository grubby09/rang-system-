import discord
from discord.ext import commands

class Clear(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(aliases=['Clear'])
  async def clear(self, ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="Info",
                          description=f':dagger: Es wurden {amount} nachrichten gelöscht!',
                          color=0xeebb17)
    await ctx.send(embed=embed)
    
def setup(bot):
  bot.add_cog(Clear(bot))
  print('\033[32mclear wurde geladen \033[0m')