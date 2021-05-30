import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_cmd_channel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def set_cmd_channel(ctx, channel: discord.TextChannel=None):
    collection = db[f"{ctx.guild.id}"]
    collection.update_one({"guild_id": ctx.guild.id}, {"$set":{"cmd":channel.id}})
    await ctx.send("Der neue Command Channel ist " + channel.name + ".")
    
def setup(bot):
  bot.add_cog(Set_cmd_channel(bot))
  print('\033[32mset cmd channel wurde geladen \033[0m')