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

    

    @group.command(name="cogfunctest", description="A test to see your cognitive functions!")
    async def cogfunctest(self, ctx, 
                          #Ti Questions
                          question1: discord.Option(float, description="You have an internal logical system for thinking that gets revised as you learn new things", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question2: discord.Option(float, description="You develop your own methods and strategies for problem solving", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question3: discord.Option(float, description="You are open to new insights and perspectives to perfect an idea", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          
                          #Te Questions
                          question4: discord.Option(float, description="Making sure people have the resources they need to succeed is very important to you.", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question5: discord.Option(float, description="You like to rely on ONLY the facts and data when making a decision", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question6: discord.Option(float, description="You are very results-oriented", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          
                          #Ni Questions (thanks Alex!)
                          question7: discord.Option(float, description="You are focused on a single conclusion, goal or vision", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question8: discord.Option(float, description="You are future oriented", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question9: discord.Option(float, description="You tend to have an \"aha\" moment where the solution seems to pop into your head", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          
                          #Ne Questions
                          question10: discord.Option(float, description="You are extremely interested in how the world works more than anything else.", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question11: discord.Option(float, description="You tend to come up with a lot more ideas than most", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question12: discord.Option(float, description="You are constantly focused on the various possibilities of the world", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          
                          #Si Questions
                          question13: discord.Option(float, description="Sensory and vividness plays a big role in how you recall memories", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question14: discord.Option(float, description="Tradition is very important to you", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question15: discord.Option(float, description="You use past experiences to understand the present", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),

                          #Se Questions (thanks Alex!)
                          question16: discord.Option(float, description="You seek sensory experience such as thrill or eating tasty food to get a physical response", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question17: discord.Option(float, description="You are unlikely to miss something in your surroundings", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question18: discord.Option(float, description="You live in the moment, not the past, not the future", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),

                          #Fi Questions (thanks Alex!)
                          question19: discord.Option(float, description="You make decisions based on what your believe to be morally correct or incorrect", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question20: discord.Option(float, description="You are very in tune with your emotions and can tell what each feeling means", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question21: discord.Option(float, description="You value being authentic to who you are", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),

                          #Fe Questions (thanks Alex!)
                          question22: discord.Option(float, description="You are very mindful of others needs and emotions in decision making", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question23: discord.Option(float, description="You tend to sacrifice your own needs and desires for others", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)]),
                          question24: discord.Option(float, description="You respect social and cultural norms", choices=[discord.OptionChoice(name="Extremely Disagree", value=0), discord.OptionChoice(name="Kinda Disagree", value=0.5), discord.OptionChoice(name="Neutral", value=1), discord.OptionChoice(name="Kinda Agree", value=1.5), discord.OptionChoice(name="Extremely Agree", value=2)])):
                          
          tiscore = 0
          tescore = 0
          niscore = 0
          nescore = 0
          siscore = 0
          sescore = 0
          fiscore = 0
          fescore = 0

          tiscore = tiscore + question1 + question2 + question3
          tescore = tescore + question4 + question5 + question6
          niscore = niscore + question7 + question8 + question9
          nescore = nescore + question10 + question11 + question12
          siscore = siscore + question13 + question14 + question15
          sescore = sescore + question16 + question17 + question18
          fiscore = fiscore + question19 + question20 + question21
          fescore = fescore + question22 + question23 + question24

          tiscore = tiscore * 10
          tescore = tescore * 10
          niscore = niscore * 10
          nescore = nescore * 10
          siscore = siscore * 10
          sescore = sescore * 10
          fiscore = fiscore * 10
          fescore = fescore * 10

          embed = discord.Embed(
                title="Your Cognitive Function test results",
                description="""
                Ti Score (Introverted Thinking): {0}
                Te Score (Extraverted Thinking): {1}
                Ni Score (Introverted Intuition): {2}
                Ne Score (Extraverted Intuition): {3}
                Si Score (Introverted Sensing): {4} 
                Se Score (Extroverted Sensing): {5}
                Fi Score (Introverted Feeling): {6}
                Fe Score (Extraverted Feeling): {7}

                """.format(tiscore, tescore, niscore, nescore, siscore, sescore, fiscore, fescore),
                color=discord.Colour.blurple(),
          )
          embed.add_field(name="Create your Stack", value="To create your stack, take your top two highest functions (referred to in this case as Dominant and Secondary) and put them into **/mbtifinder** to get your MBTI and full stack! (NOTE: There is some criteria involved with this. Your top two functions must be one introverted and one extraverted. They also cannot be opposites, so no Ti-Fe. If this doens't work for your results then simply take the third highest or beyond.)")
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
