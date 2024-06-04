import discord
from discord.ext import commands
import os
import random
import cogs.requestHandler as handler
from random import uniform
import json
import requests

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]

with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]


#The Dev status is meant for if UltraBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "UltraBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "UltraBot"
            game = "combinesoldier14.site"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"




class Dnd(commands.Cog):
    group = discord.SlashCommandGroup(name="dnd", description="Commands relating to the board game Dungeons and Dragons")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(name="dndmodifier", description="Get info on DND modifiers!")
    async def dndmodifier(self, ctx, mod: discord.Option(str, description="The modifier to get info on", choices=["STR", "DEX", "CON", "INT", "WIS", "CHA"])):
        d = requests.get("https://www.dnd5eapi.co/api/ability-scores/{}".format(mod.lower()))
        j = json.loads(d.text)
       
        skillz = ""
        for skill in j["skills"]:
           skillz = skillz + "{}, ".format(skill["name"])
        
        if mod == "CON":
           skillz = "Skills: None"
        
        embed = discord.Embed(
            title = "{0} ({1})".format(j["full_name"], j["name"]),
            description = "{0} {1}".format(j["desc"][0], j["desc"][1]),
            color = discord.Colour.blurple(),
        )
        embed.set_footer(text="Skills: {}".format(skillz))
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Purple_d20.png")
        await ctx.respond(embed=embed)
        
        








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Dnd(bot)) # add the cog to the bot
