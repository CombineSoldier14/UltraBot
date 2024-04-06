import discord
import os # default module
from discord.ext import commands
import json

# Defing bot and bot user intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)



#This file main.py can be seen as a cog itself. Only basic commands are here!

@bot.event
async def on_ready():
    print("UltraBot.py is up and running!")

# say is intentionally not a slash command.
#Don't worry, the french people joke is an inside joke with my friend
@bot.command(name="say")
async def _say(ctx, text):
    
    await ctx.send(text)
    await ctx.message.delete()

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    with open("token.json", "r") as f:
      _d = json.load(f)
    bot.run(_d["BOT_TOKEN"])
