import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class On_guild_join(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    collection = db[f"{str(guild.id)}"]
    collection.drop()

    
def setup(bot):
  bot.add_cog(On_guild_join(bot))
  print('\033[32mon guild remove wurde geladen \033[0m')