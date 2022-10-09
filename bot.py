import discord 
from discord.ext import commands 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
  print('The bot is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send('Fuck off Jared!')

bot.run('MTAyODA5ODM4NjIxMTExNTAyOA.Gls6WK.40OiRuJdD26OzOx4Jg6HF2rwgqDyZZXuDuBXgY')