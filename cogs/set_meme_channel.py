import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_meme_channel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def set_meme_channel(self, ctx, channel: discord.TextChannel=None):
    collection = db[f"{ctx.guild.id}"]
    for v in collection.find({"guild_id": ctx.guild.id}):
      collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"meme": channel.id}})
      await ctx.send("Der neue Meme Channel ist " + channel.name)
      
def setup(bot):
  bot.add_cog(Set_meme_channel(bot))
  print('\033[32mset meme channel wurde geladen \033[0m')