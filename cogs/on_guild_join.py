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
    db.create_collection(f"{guild.id}")
    collection = db[f"{str(guild.id)}"]
    liste = {"guild_name": guild.name, "guild_id": guild.id, "cmd": "None", "meme": "None", "join": "None", "leave": "None", "logs": "None", "tick_mess_reac": "None", "tick_chan": "None", "join_mess": "None", "leave_mess": "None"}
    collection.insert_one(liste)

    
def setup(bot):
  bot.add_cog(On_guild_join(bot))
  print('\033[32mon guild join wurde geladen \033[0m')