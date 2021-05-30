import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Set_ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def set_ticket(ctx, channel: discord.TextChannel=None):
    collection = db[f"{channel.guild.id}"]
    for t in collection.find({"guild_id": ctx.guild.id}):
      mess = await channel.send(embed=discord.Embed(title="Support", description="Reagiere mit 📩 um ein Ticket zu  eröffnen.", color=discord.Color.green()))
      await mess.add_reaction("📩")
      collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"tick_mess_reac": mess.id}})
      collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"tick_chan": mess.id}})
      await ctx.send("Der neue ticket Channel ist " + channel.name)
      
  @set_ticket.error
  async def set_ticket_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("Dir Fehlt die Berechtigung Channel zu bearbeiten.")
    if isinstance(error, commands.ChannelNotFound):
      await tcx.send("Dieser Channel wurde nicht gefunden")

def setup(bot):
  bot.add_cog(Set_ticket(bot))
  print('\033[32mset ticket wurde geladen \033[0m')