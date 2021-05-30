import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_leave_channel(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def set_leave_channel(self, ctx, new_channel: discord.TextChannel=None, *, message=None, member: discord.Member=None):
    if new_channel != None and message != None:
        for channel in ctx.guild.channels:
            if channel == new_channel:
              collection = db[f"{ctx.guild.id}"]
              collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"leave_mess": str(message)}})
              collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"leave": new_channel.id}})
              await ctx.send("Der neue Willkommens Channel ist " + new_channel.mention + " und der NAchricht " + message)
              await new_channel.send("In diesen Kanal werden absofort Nahrichten kommem wenn eine Persohn den Server verlässt.")
  
  @set_leave_channel.error
  async def set_leave_channel_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("Du hast keine Berechtigung Diesen Befehl zu nutzen")
    if isinstance(error, commands.ChannelNotFound):
      await ctx.send("Dieser Channel wurde nicht gefunden")
      
def setup(bot):
  bot.add_cog(Set_leave_channel(bot))
  print('\033[32mset leave channel wurde geladen \033[0m')