import discord
from discord.ext import commands
from pymongo import MongoClient
import aiohttp
import random

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

class Meme(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def meme(self, ctx):
    collection = db[f"{ctx.guild.id}"]
    for v in collection.find({"guild_id": ctx.guild.id}):
      meme = ctx.guild.get_channel(v["meme"])
      if v["meme"] == "None":
        embed = discord.Embed(colour=discord.Colour.green(), title="""Here's a meme""")
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])

            await ctx.send(embed=embed)
      else:
        if ctx.channel.id == v["meme"]:
          embed = discord.Embed(colour=discord.Colour.green(), title="""Here's a meme""")
          async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
              res = await r.json()
              embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])

              await ctx.send(embed=embed)
        else:
          await ctx.send(embed=discord.Embed(description="Du kanns nur in " + meme.mention + " diesen command ausführen"))
              
def setup(bot):
  bot.add_cog(Meme(bot))
  print('\033[32mmeme wurde geladen \033[0m')