import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class On_message(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_message(self, message):
    collection = db[f"{message.guild.id}"]
    for h in collection.find({"guild_id": message.guild.id}):
      count_ = message.guild.get_channel(h["count"])
      if h["count"] == "None":
        pass
      else:
        if message.channel.id == h["count"]:
          c_channel = discord.utils.get(message.guild.text_channels, name=count_.name)
          messages = await c_channel.history(limit=2).flatten()
          if message.content.isnumeric():
            if message.channel == c_channel and int(messages[1].content) + 1 != int(message.content):
              await message.delete()
            else:
              await message.add_reaction("✔")
          else:
            await message.delete()
        
def setup(bot):
  bot.add_cog(On_message(bot))
  print('\033[32mon message wurde geladen \033[0m')