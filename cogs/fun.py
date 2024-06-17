import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import cowsay
import nltk
import random
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION


nltk.download('words')

word_list = ["Heads", "Tails"]
eightball_list = ["It is certain.", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]



class Fun(commands.Cog):
    group = discord.SlashCommandGroup(name="fun", description="Commands made for having fun!")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.quotes = [
                       """
                       > *"Almost Christmas means it wasn't christmas!"* 
                       - Phoenix Wright, *Phoenix Wright: Ace Attorney*
                       """,
"""
> *"You are not just a clown. You are the entire circus"* 
- Miles Edgeworth, *Ace Attorney: Justice for All*
""",
"""
> *"Let's see those molars, Wright."*
- Miles Edgeworth
""",
"""
> *"That's it! I'm not doing a single cent of my taxes!"*
- Ema Skye, *Ace Attorney: Spirit of Justice*
""",
"""
> *"If you mess with The Best you will fall like the rest!"*
- Sebastian Debeste, *Ace Attorney: Investigations 2*
""",
"""
> *"If the pee ain't clear, death is near!"*
- Sebastian Debeste, *Ace Attorney: Investigations 2*
""",
"""
> *"Let's be scientific about this, please! Just put it in your pocket"*
- Ema Skye, *Phoenix Wright: Ace Attorney*
""",
"""
> *"You are the most foolishly foolish fool of a fool I have ever seen, Mr. Phoenix Wright!"*
- Franziska von Karma, *Ace Attorney: Justice for All*
""",
"""
> *"Blacker than a moonless night, hotter and more bitter than hell itself, that is coffee."*
- Godot *Ace Attorney: Trials and Tribulations*
""",
"""
> *"I'm Apollo Justice and I'm FINE!!!!"*
- Apollo Justice, *Ace Attorney: Dual Destinies*
""",
"""
> *"Apollo, tie me up in a new pose! Wait, you're not into this kinda thing, are you...?"*
- Athena Cykes, *Ace Attorney: Dual Destinies*
""",
"""
> *"You've come to the Wright place!"*
- Trucy Wright, *Apollo Justice: Ace Attorney*
""",
"""
> *"It appears the witness had several... sugar daddies."*
- Winston Payne, *Phoenix Wright: Ace Attorney*
""",
"""
> *"When something smells, it's usually the Butz*"
- Phoenix Wright, *Phoenix Wright: Ace Attorney*
""",
"""
> *"In justice we TRUST!"*
- Bobby Fulbright, *Ace Attorney: Dual Destinies*
""",
"""
> *"You asked for the enlargement, you got the enlargement."*
- Manfred von Karma, *Phoenix Wright: Ace Attorney*
""",
"""
> *"Say \"Hi\", for me, ok? Oh, and '/screw you'/."*
- Daryan Crescend, *Apollo Justice, Ace Attorney*
""",
"""
> *"The miracle never happen."*
- Phoenix Wright, *Ace Attorney: Justice for All*
""",
"""
> *"Oh, I assure you, it's quite based."*
- Phoenix Wright, *Apollo Justice: Ace Attorney*
""",
"""
> *"Why can't we have a normal, straightforward killing once in a while in this country?"*
- Ema Skye, *Apollo Justice: Ace Attorney*
""",
"""
> *"A lawyer only cries once it's all over."*
- Diego Armando/||Godot||
""",
"""
> *"This place is so fruity!"*
- Maya Fey, *Ace Attorney: Trials and Tribulations*
""",
"""
> *"I must say I'm used to being inspected by the ladies, but this is the first time I've felt this way with a man."*
- Klavier Gavin, *Apollo Justice: Ace Attorney*]
"""]    
    @group.command(name="cowsay", description="The cowsay command from Linux!")
    async def cowsay(self, ctx, text=discord.Option(str, description="Text for cow to say", required=True), 
                     character=discord.Option(str, description="Character for cowsay to use."), 
                     choices=cowsay.char_names, default="cow"):
        await ctx.respond("```\n{0}\n```".format(cowsay.get_output_string(character, text))),
    
    @group.command(name="randomword", description="Gives you a random English word!")
    async def randomword(self, ctx):
        await ctx.respond("Your Random Word: `" + random.choice(nltk.corpus.words.words()) + "`")
    
    @group.command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, ctx):
        await ctx.respond(":coin: **" + random.choice(word_list) + "**")

    @group.command(name="8ball", description="The Magic 8 Ball answers your question!")
    async def _8ball(self, ctx, text=discord.Option(str, description="Question to ask the 8 ball")):
        embed = discord.Embed(
            title="Magic 8 Ball: " + text,
            description=random.choice(eightball_list),
            color=discord.Colour.darker_gray(),
            
        )
        embed.set_thumbnail(url="https://icons.iconarchive.com/icons/barkerbaggies/pool-ball/256/Ball-8-icon.png")
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
        await ctx.respond(embed=embed)

    @group.command(name="randomyt", description="Get a random youtube video")
    async def randomyt(self, ctx):
         await ctx.respond(cogs.combinebot.getYTvideo())
         await ctx.send("NOTE: Not all generated videos may exist.")

    @group.command(name="aaquote", description="Get a random Ace Attorney quote!")
    async def aaquote(self, ctx):
          await ctx.respond(
                cogs.combinebot.getAceAttorneyQuote()
          )

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot

