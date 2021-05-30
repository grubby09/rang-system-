import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Kick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.guild_only()
  async def kick(self, ctx, member: discord.Member=None, reason=None):
    collection = db[f"{ctx.guild.id}"]
    for v in collection.find({"guild_id": ctx.guild.id}):
      print(v["cmd"])
      cmd = ctx.guild.get_channel(v["cmd"])
      if v["cmd"] == "None" and v["logs"] == "None":
        await ctx.send(embed=discord.Embed(description=f"Benutzer {member} wurde Gebannt mit den Grund: {reason}!"))
        await member.kick(reason=reason)
      elif v["cmd"] == "None":
        await ctx.send(embed=discord.Embed(description=f"Benutzer {member} wurde Gebannt mit den Grund: {reason}!"))
        await member.kick(reason=reason)
      else:
        print("nidawuo")
        if ctx.channel.id == v["cmd"]:
          await ctx.send(embed=discord.Embed(description=f"Benutzer {member} wurde Gebannt mit den Grund {reason}"))
          await member.kick(reason=reason)
        else:
          await ctx.send(embed=discord.Embed(description="Du kanns nur in " + cmd.mention + " diesen command ausführen"))

def setup(bot):
  bot.add_cog(Kick(bot))
  print('\033[32mkick wurde geladen \033[0m')