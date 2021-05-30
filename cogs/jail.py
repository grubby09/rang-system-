import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Jail(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def jail(self, ctx, member: discord.Member=None):
    collection = db[f"{ctx.guild.id}"]
    for v in collection.find({"guild_id": ctx.guild.id}):
      cmd = ctx.guild.get_channel(v["cmd"])
      if v["cmd"] == "None":
        role = discord.utils.get(ctx.guild.roles, name="Jail")
        if not role in ctx.guild.roles:
          await ctx.guild.create_role(name="Jail")
          await ctx.send("Der Benutzer " + member.mention + " wurde in den Knast gesteckt")
          await member.add_roles(role)
          return
        else:
          if not role in member.roles:
            await ctx.send("Der Benutzer " + member.mention + " wurde in den Knast gesteckt")
            await member.add_roles(role)
            return
          else:
            await ctx.send("Der Benutzer ist schon im knast.")
            return
    else:
      if ctx.channel.id == v["count"]:
        role = discord.utils.get(ctx.guild.roles, name="Jail")
        if not role in ctx.guild.roles:
          await ctx.guild.create_role(name="Jail")
          await ctx.send("Der Benutzer " + member.mention + " wurde in den Knast gesteckt")
          await member.add_roles(role)
          return
        else:
          if not role in member.roles:
            await ctx.send("Der Benutzer " + member.mention + " wurde in den Knast gesteckt")
            await member.add_roles(role)
            return
          else:
            await ctx.send("Der Benutzer ist schon im knast.")
            return
      else:
        await ctx.send("Du kannst diesen Command nur in " + cmd.mention + " nutzen")

def setup(bot):
  bot.add_cog(Jail(bot))
  print('\033[32mjail wurde geladen \033[0m')