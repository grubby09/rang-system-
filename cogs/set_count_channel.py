import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_count_channel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def set_count_channel(self, ctx, channel: discord.TextChannel=None):
    collection = db[f"{ctx.guild.id}"]
    collection.update_one({"guild_id": ctx.guild.id}, {"$set":{"count": channel.id}})
    await ctx.send("Der neue Counter Channel ist " + channel.mention + ".")
    reac = await channel.send("1")
    await reac.add_reaction("✔")
    
  @set_count_channel.error
  async def set_join_channel_error(ctx, error):
    if isinstance(error, commands.ChannelNotFound):
      await ctx.send("Der Channel wurde nicht gefunden")
    else:
      pass
    
def setup(bot):
  bot.add_cog(Set_count_channel(bot))
  print('\033[32mset count channel wurde geladen \033[0m')