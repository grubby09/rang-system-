import discord
from discord.ext import commands
import os
from pymongo import MongoClient

client = MongoClient('mongodb://discordbot:ZPkSJ6G0BuaYlPQH9QDVpAFNgeLwVCMT8oWRJTMvYUKROGSO54xWBhL3ZfKdtiq1nEXzXNsrmAIbcDHE7CFUj2yI@194.93.56.238:27017/discordbot')

db = client["discordbot"]

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print(f"Bot-name: {bot.user}\nBot-id: {bot.user.id}\nServers: {len(bot.guilds)}")
  
@bot.command()
async def load(ctx, cog: str):
  if ctx.author.id == 716580823448420354:
    if cog + ".py" in os.listdir("./cogs"):
      bot.load_extension("cogs." + cog)
      await ctx.send("Die datei wurde geladen!")
    else:
      await ctx.send("Diese datei existiert nicht!")
  else:
    await ctx.send("Du bist nicht der Owner des bots!")
    
  
@bot.command()
async def unload(ctx, cog: str):
  if ctx.author.id == 716580823448420354:
    if cog + ".py" in os.listdir("./cogs"):
      bot.unload_extension("cogs." + cog)
      await ctx.send("Die datei wurde entladen!")
    else:
      await ctx.send("Diese datei existiert nicht!")
  else:
    await ctx.send("Du bist nicht der Owner des bots!")
    
@bot.command()
async def loadall(ctx):
  if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            if filename != "locales.py":
                bot.load_extension(f'cogs.{filename[:-3]}')
        
@bot.command()
async def unloadall(ctx):
  if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            if filename != "locales.py":
                bot.unload_extension(f'cogs.{filename[:-3]}')
                
@bot.command()
async def info(ctx):
  collection = db[f"{ctx.guild.id}"]
  for v in collection.find({"guild_id": ctx.guild.id}):
    await ctx.send(v)

bot.run("ODM1MTM3NDM0ODk0MzM2MDEx.YILEWA.lCDJYMNaS6pNE4prFI7qcwRaESE")