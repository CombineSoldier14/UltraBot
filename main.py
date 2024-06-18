import discord
import os # default module
from discord.ext import commands
import json
import logging
import cowsay
from discord import Option
from discord import User
from discord import Interaction
from discord import InteractionResponse
from discord import MessageInteraction
from discord import interactions
from discord import InteractionMessage
import nltk
import random
import cogs.combinebot


with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]


with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

with open("latestaddition.json", "r") as f:
            _r = json.load(f)
            LATESTADDITION = _r["LATEST_ADDITION"]


#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"
            prefix = "-"
            link = "https://discord.com/oauth2/authorize?client_id=1227477531461025854"


if dev_status == "false":
            name = "CombineBot"
            game = "https://combinebot.blogspot.com/"
            icon = "https://i.postimg.cc/j5YGqs0n/f66bd4beb4f1ebee0685d8c5cfd646bb.png"
            prefix = ";"
            link = "https://discord.com/oauth2/authorize?client_id=1225220764861730867"



nltk.download('words')


FRENCH = 420052952686919690




# Defing bot and bot user intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

logging.basicConfig(level=logging.INFO)
#loading cogs
bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.apis')
bot.load_extension('cogs.mbti')
bot.load_extension('cogs.calculator')
bot.load_extension('cogs.rps')
bot.load_extension('cogs.utilitycog')
bot.load_extension('cogs.role')
bot.load_extension('cogs.mcstatus')
bot.load_extension('cogs.suntzu')
bot.load_extension('cogs.cogfunc')
bot.load_extension('cogs.dnd')
bot.load_extension('cogs.cogfunctest')
bot.load_extension('cogs.enneagramtest')
bot.load_extension('cogs.mbtitest')



@bot.event
async def on_ready():
    status = discord.Game(game)
    await bot.change_presence(activity=status)
    bot.auto_sync_commands = True
    logging.info("Bot is ready!")
    

class ProblemView(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

      supportServerButton = discord.ui.Button(label="Report GitHub issue", style=discord.ButtonStyle.gray, url="https://github.com/CombineSoldier14/CombineBot/issues/new")
      self.add_item(supportServerButton)


@bot.event
async def on_application_command_error(interaction: discord.Interaction,
                                        error: discord.DiscordException):
    embed = discord.Embed(
        title = "Whoops!",
        description = "An error has occured.  Retrying the command might help, or this can be an internal server error",
        color = discord.Colour.red()
    )
    embed.add_field(name="Error Message", value="`{0}`".format(repr(error)))

    embed.set_thumbnail(url="https://i.imgur.com/KR3aiwB.png")
    try:
        await interaction.response.send_message(embed=embed, view=ProblemView())
    except:
        await interaction.followup.send(embed=embed, view=ProblemView())
    raise error

#CombineBot website button for /about
class AboutLinkBloggerView(discord.ui.View):
    def __init__(self):
     super().__init__(timeout=None)

     supportServerButton = discord.ui.Button(label='Learn More!', style=discord.ButtonStyle.gray, url='https://combinebot.blogspot.com/')
     self.add_item(supportServerButton)

     supportServerButton = discord.ui.Button(label='GitHub', style=discord.ButtonStyle.gray, url='https://github.com/CombineSoldier14/CombineBot')
     self.add_item(supportServerButton)

     supportServerButton = discord.ui.Button(label='Add {0}!'.format(name), style=discord.ButtonStyle.gray, url=link)
     self.add_item(supportServerButton)
    
class InviteView(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

      supportServerButton = discord.ui.Button(label="Invite CombineBot!", style=discord.ButtonStyle.gray, url="https://discord.com/oauth2/authorize?client_id=1225220764861730867")
      self.add_item(supportServerButton)


#This file main.py can be seen as a cog itself. Only basic commands are here!





@bot.slash_command(name="ping", description="Sends the bot's ping or latency")
async def ping(ctx):
    await ctx.respond("Pong! Latency or ping is {0}".format(round(bot.latency * 100, 2)))

@bot.slash_command(name="helloworld", description="If your program can't say this, don't talk to me")
async def helloworld(ctx):
    await ctx.respond("Hello world!")





@bot.slash_command(name="about", description="About the bot")
async def about(ctx):
    embed = discord.Embed(
        title= "About " + name + " v" + VERSION,
        description= "{0} is a Python based discord bot created by CombineSoldier14 with commands for moderation and fun!\n CombineBot's birthday is **4/5/2024.**".format(name),
        color=discord.Colour.yellow(),
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="**Latest Addition**", value=LATESTADDITION)
    embed.add_field(name="**Bot Ping**", value="{0} ms".format(round(bot.latency * 100, 2)))
    await ctx.respond(embed=embed, view=AboutLinkBloggerView())


# say is intentionally not a slash command.
#The french people joke is an inside joke with my friends. I'm not racist! :)
@bot.command(name="say")
async def _say(ctx, *, args):
    if ctx.author.id == FRENCH:
        await ctx.send("\n> *:middle_finger: \"You can go fuck yourself with that!*\" -Brewstew")
        await ctx.message.delete()
    else:
      await ctx.send(args)
      await ctx.message.delete()

@bot.slash_command(name="ephemeral", description="Sends an ephemeral message to yourself!")
async def ephemeral(ctx, text):
    await ctx.respond(text, ephemeral="true")
    
@bot.slash_command(name="spoiler", description="Marks your text as a spoiler!")
async def _spoiler(ctx, text):
    
    await ctx.respond("||" + text + "||")
    

@bot.slash_command(name="invite", description="Get the invite link for CombineBot!")
async def invite(ctx):
   await ctx.respond(view=InviteView())

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    if os.path.isfile("token.json") == True: # check if token.json exists
        with open("token.json", "r") as f:
            _d = json.load(f)
            loadedJSONToken = _d["BOT_TOKEN"]
        if loadedJSONToken.lower() == "yourtokenhere":
            loadedJSONToken = None
    else:
        loadedJSONToken = None
    environToken = os.getenv("BOT_TOKEN")

    if (loadedJSONToken == None) and (environToken == None):
        raise EnvironmentError("No token specified!  Please enter a token via token.json or by passing an environment variable called 'BOT_TOKEN'.  Stop.")
    BOT_TOKEN = (environToken if environToken != None else loadedJSONToken)    
    bot.run(BOT_TOKEN)














