import discord
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Unban(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(ban_members=True, kick_members=True)
  async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
        collection = db[f"{ctx.guild.id}"]
        for v in collection.find({"guild_id": ctx.guild.id}):
          cmd = ctx.guild.get_channel(v["cmd"])
          if v["cmd"] == "None" and v["logs"] == "None":
            await ctx.send(embed=discord.Embed(description="Der Benutzer " + user + " wurde entbannt."))
            await ctx.guild.unban(user)
          else:
            if ctx.channel.id == v["cmd"]:
              await ctx.send(embed=discord.Embed(description=f"Benutzer {member} wurde Gebannt mit den Grund {reason}"))
              await ctx.guild.unban(user)
            else:
              await ctx.send(embed=discord.Embed(description="Du kanns nur in " + cmd.mention + " commands ausführen"))
              
def setup(bot):
  bot.add_cog(Unban(bot))
  print('\033[32munban wurde geladen \033[0m')