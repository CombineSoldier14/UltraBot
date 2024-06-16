import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime

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


if dev_status == "false":
            name = "CombineBot"
            game = "combinesoldier14.site"
            icon = "https://i.postimg.cc/j5YGqs0n/f66bd4beb4f1ebee0685d8c5cfd646bb.png"
            prefix = ";"


def makeEmbed(title, description, color):
        embed = discord.Embed(
                title=title,
                description=description,
                color=color
        )
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon) 
        return embed
        

































