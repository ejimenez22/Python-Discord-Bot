import discord 
from discord.ext import commands 
import os
from dotenv import load_dotenv

load_dotenv()

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))


bot.run(os.getenv("TOKEN"))