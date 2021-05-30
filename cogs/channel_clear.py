import discord
from discord.ext import commands
import asyncio

class Channel_clear(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def channel_clear(ctx):
    channelid = ctx.channel.id
    channel1 = self.bot.get_channel(channelid)
    await channel1.clone()
    asyncio.sleep(2)
    await channel1.delete()
    
def setup(bot):
  bot.add_cog(Channel_clear(bot))
  print('\033[32mchannel clear wurde geladen \033[0m')