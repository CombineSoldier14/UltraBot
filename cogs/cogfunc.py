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


#The Dev status is meant for if UltraBot is running in DEV mode which changes some names and icons.

if dev_status == "true":
            name = "UltraBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "UltraBot"
            game = "combinesoldier14.site"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"





class Cogfunc(commands.Cog):
    group = discord.SlashCommandGroup(name="cogfunc", description="Commands relating to the Myers-Briggs Type Indicator cognitive functions system")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @group.command(title="cogfunctest", description="A test that shows your scores of each Cognitive Function")
    async def cogfunctest(self, ctx, 
                          
                          #Ti vs Fe questions
                          question1: discord.Option(str, description="Do you like to analyze things more around you or abide by social norms more?", choices=["Analyze things", "Abide by social norms"]),
                          question2: discord.Option(str, description="Do you focus on internalizing everything more or making others happy more?", choices=["Internalizing things", "Making others happy"]),
                          question3: discord.Option(str, description="Do you quietly ponder things or are you sensitive to the feelings of others?", choices=["Quietly ponder things", "Feelings of others"]),
                          
                          #Te vs Fi questions
                          question4: discord.Option(str, description="Do you focus on efficency more or focus on empathy more?", choices=["Efficency", "Empathy"]),
                          question5: discord.Option(str, description="Do you make decisions off of reasons and research more or what you feel in the moment more?", choices=["Reasons and research", "Feel in the moment"]),
                          question6: discord.Option(str, description="Are you more persuasive or do you feel others emotions more?", choices=["Persuasive", "Feel others emotions"]),
                          
                          #Si vs Ne questions
                          question7: discord.Option(str, description="Do you rely more on past experiences more or on making new stuff more?", choices=["Past experiences", "Making new stuff"]),
                          question8: discord.Option(str, description="Have you been described more as stubborn or more as an idea machine?", choices=["Stubborn", "Idea Machine"]),
                          question9: discord.Option(str, description="Do you follow tradition more or notice patterns more?", choices=["Follow tradition", "Notice patterns"]),
                          
                          #Se vs Ni questions
                          question10: discord.Option(str, description="Do you spend more time pleasing the senses or achieving your goals?", choices=["Pleasing senses", "Achieving goals"]),
                          question11: discord.Option(str, description="When navigating the world, do you rely more on instincts or more on details?", choices=["Instincts", "Details"]),
                          question12: discord.Option(str, description="Do you spend more time thinking inwardly or more time living in the moment?", choices=["Thinking inwardly", "Living in the moment"])):
            presitotal = 0
            presetotal = 0
            prenitotal = 0
            prenetotal = 0
            prefitotal = 0
            prefetotal = 0
            pretitotal = 0
            pretetotal = 0

            if question1 == "Analyze things":
                    pretitotal += 1
            else:
                    prefetotal += 1

            if question2 == "Internalizing things":
                    pretitotal += 1
            else:
                    prefetotal += 1

            if question3 == "Quietly ponder things":
                    pretitotal += 1
            else:
                    prefetotal += 1

           
            if question4 == "Efficency":
                    pretetotal += 1
            else:
                    prefitotal += 1

            if question5 == "Reasons and research":
                    pretetotal += 1
            else:
                    prefitotal += 1

            if question6 == "Persuasive":
                    pretetotal += 1
            else:
                    prefitotal += 1

            if question7 == "Past experiences":
                    presitotal += 1
            else:
                    prenetotal += 1

            
            if question8 == "Stubborn":
                    presitotal += 1
            else:
                    prenetotal += 1

            if question9 == "Follow tradition":
                    presitotal += 1
            else:
                    prenetotal += 1

            
            if question10 == "Pleasing senses":
                    presetotal += 1
            else:
                    prenitotal += 1

            if question11 == "Details":
                    presetotal += 1
            else:
                    prenitotal += 1

            if question12 == "Living in the moment":
                    presetotal += 1
            else:
                    prenitotal += 1

            presitotal2 = round(presitotal, 1)
            presetotal2 = round(presetotal, 1)
            prenitotal2 = round(prenitotal, 1)
            prenetotal2 = round(prenetotal, 1)
            prefitotal2 = round(prefitotal, 1)
            prefetotal2 = round(prefetotal, 1)
            pretitotal2 = round(pretitotal, 1)
            pretetotal2 = round(pretetotal, 1)

            sitotal = presitotal2 * 10
            setotal = presetotal2 * 10
            nitotal = prenitotal2 * 10
            netotal = prenetotal2 * 10
            fitotal = prefitotal2 * 10
            fetotal = prefetotal2 * 10
            titotal = pretitotal2 * 10
            tetotal = pretetotal2 * 10

            embed = discord.Embed(
                    title="Your Cognitive Functions",
                    description="""
                    Ti Score _(Introverted Thinking)_: **{0}**
                    Te Score _(Extroverted Thinking)_: **{1}**
                    Fi Score _(Introverted Feeling)_: **{2}**
                    Fe Score _(Extroverted Feeling)_: **{3}**
                    Ni Score _(Introverted Intuition)_: **{4}**
                    Ne Score _(Extroverted Intuition)_: **{5}**
                    Si Score _(Introverted Sensing)_: **{6}**
                    Se Score _(Extroverted Sensing)_: **{7}**

                    _To create your function stack, take your top two functions (They cannot be opposites, so no Ti-Fe. If your second function is the opposite of your highest, then just choose your third highest. It also must go introvert-extrovert or vice versa. They also cannot be the same type of function, so no Ti-Te.) and put them in a dashed line like this:_

                    `topfunction-secondfunction`

                    _Then, put the opposites of your second and top functions as the third and fourth functions respectively in your stack, so it should look like this:_

                    `topfunction-secondfunction-oppositesecond-oppositetop`

                    _For example, if your highest is Ti and second highest is Se then your stack would look like this:_

                    `Ti-Se-Ni-Fe`

                    """.format(titotal, tetotal, fitotal, fetotal, nitotal, netotal, sitotal, setotal),
                    color=discord.Colour.blurple(),
                    


            )
            embed.set_footer(text="The higher the number, the more of that function you have.")

            await ctx.respond(embed=embed)

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
