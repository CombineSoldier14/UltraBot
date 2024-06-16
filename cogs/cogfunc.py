import discord
from discord.ext import commands
import os
import json

mbtilist=["INTJ", "ENTJ", "INTP", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ESTJ", "ISFJ", "ESFJ", "ISTP", "ESTP", "ISFP", "ESFP"]

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]


with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]


#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "CombineBot"
            game = "combinesoldier14.site"
            icon = "https://i.postimg.cc/j5YGqs0n/f66bd4beb4f1ebee0685d8c5cfd646bb.png"




class Cogfunc(commands.Cog):
    group = discord.SlashCommandGroup(name="cogfunc", description="Commands relating to the Myers-Briggs Type Indicator cognitive functions system")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    

    
          
          

    @group.command(title="mbtifinder", description="Tells you an MBTI via specified dominant/secondary functions.")
    async def mbtifinder(self, ctx, dom: discord.Option(str, description="Dominant function", choices=["Ti", "Te", "Fi", "Fe", "Si", "Se", "Ni", "Ne"]), sec: discord.Option(str, description="Secondary function", choices=["Ti", "Te", "Fi", "Fe", "Si", "Se", "Ni", "Ne"])):
            if dom == "Ti" and sec == "Se":
                    mbti = "ISTP"
                    stack = "Ti-Se-Ni-Fe"

            elif dom == "Ti" and sec == "Ne":
                    mbti = "INTP"
                    stack = "Ti-Ne-Si-Fe"

            elif dom == "Te" and sec == "Si":
                    mbti = "ESTJ"
                    stack = "Te-Si-Ne-Fi"

            elif dom == "Te" and sec == "Ni":
                    mbti = "ENTJ"
                    stack = "Te-Ni-Se-Fi"

            elif dom == "Fi" and sec == "Se":
                    mbti = "ISFP"
                    stack = "Fi-Se-Ni-Te"

            elif dom == "Fi" and sec == "Ne":
                    mbti = "INFP"
                    stack = "Fi-Ne-Si-Te"

            elif dom == "Fe" and sec == "Si":
                    mbti = "ESFJ"
                    stack = "Fe-Si-Ne-Ti"

            elif dom == "Fe" and sec == "Ni":
                    mbti = "ENFJ"
                    stack = "Fe-Ni-Se-Ti"

            elif dom == "Si" and sec == "Te":
                    mbti = "ISTJ"
                    stack = "Si-Te-Fi-Ne"

            elif dom == "Si" and sec == "Fe":
                    mbti = "ISFJ"
                    stack = "Si-Fe-Ti-Ne"

            elif dom == "Se" and sec == "Ti":
                    mbti = "ESTP"
                    stack = "Se-Ti-Fe-Ni"

            elif dom == "Se" and sec == "Fi":
                    mbti = "ESFP"
                    stack = "Se-Fi-Te-Ni"

            elif dom == "Ni" and sec == "Te":
                    mbti = "INTJ"
                    stack = "Ni-Te-Fi-Se"

            elif dom == "Ni" and sec == "Fe":
                    mbti = "INFJ"
                    stack = "Ni-Fe-Ti-Se"

            elif dom == "Ne" and sec == "Ti":
                    mbti = "ENTP"
                    stack = "Ne-Ti-Fe-Si"

            elif dom == "Ne" and sec == "Fi":
                    mbti = "ENFP"
                    stack = "Ne-Fi-Te-Si"

            else:
                    await ctx.respond(":x: That function pair is invalid. Remember, they cannot be the same type (so no Ti-Te), they cannot be opposites (so no Ti-Fe), and they must be introvert-extrovert or vice versa.")
                    return

            await ctx.respond("The functions **{0}**-**{1}** belong to **{2}**. The full stack is **{3}**.".format(dom, sec, mbti, stack))
                
    @group.command(name="mbtifunctions", description="Shows you the cognitive function stack for an MBTI")
    async def mbtifunctions(self, ctx, mbti: discord.Option(str, description="The MBTI to get the stack of. Will be random if left blank.", choices=mbtilist)):
        stack = ""
        if mbti == "INTJ":
            stack = "Ni-Te-Fi-Se"
        if mbti == "ENTJ":
            stack = "Te-Ni-Se-Fi"
        if mbti == "INTP":
            stack = "Ti-Ne-Si-Fe"
        if mbti == "ENTP":
            stack = "Ne-Ti-Fe-Si"
        if mbti == "INFJ":
            stack = "Ni-Fe-Ti-Se"
        if mbti == "INFP":
            stack = "Fi-Ne-Si-Te"
        if mbti == "ENFJ":
            stack = "Fe-Ni-Se-Ti"
        if mbti == "ENFP":
            stack = "Ne-Fi-Te-Si"
        if mbti == "ISTJ":
            stack = "Si-Te-Fi-Ne"
        if mbti == "ESTJ":
            stack = "Te-Si-Ne-Fi"
        if mbti == "ISFJ":
            stack = "Si-Fe-Ti-Ne"
        if mbti == "ESFJ":
            stack = "Fe-Si-Ne-Ti"
        if mbti == "ISTP":
            stack = "Ti-Se-Ni-Fe"
        if mbti == "ESTP":
            stack = "Se-Ti-Fe-Ni"
        if mbti == "ISFP":
            stack = "Fi-Se-Ni-Te"
        if mbti == "ESFP":
            stack = "Se-Fi-Te-Ni"
        await ctx.respond("The cognitive function stack for **{0}** is **{1}**.".format(mbti, stack))
            


            


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Cogfunc(bot)) # add the cog to the bot
