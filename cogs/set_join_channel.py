import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_join_channel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def set_join_channel(self, ctx, new_channel: discord.TextChannel=None, *, message=None):
    if not ctx.author.bot:
      print("Befehl ausgeführt")
      if new_channel != None and message != None:
        for channel in ctx.guild.channels:
          if channel == new_channel:
            collection = db[f"{ctx.guild.id}"]
            collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"join_mess": str(message)}})
            collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"join": new_channel.id}})
            await ctx.send("Der neue Willkommens Channel ist " + new_channel.mention + " und der NAchricht " + message)
            for g in collection .find({"guild_id": ctx.guild.id}):
              print(g)
            await new_channel.send("In diesen Channel werden absofort Nahrichten kommen wenn jemand denn Server beitritt.")

  @set_join_channel.error
  async def set_join_channel_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("Du hast keine Berechtigung Diesen Befehl zu nutzen")
    if isinstance(error, commands.ChannelNotFound):
      await ctx.send("Dieser Channel wurde nicht gefunden")

def setup(bot):
  bot.add_cog(Set_join_channel(bot))
  print('\033[32mset join channel wurde geladen\033[0m')
  
