import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime
import logging

class QuestionView(discord.ui.View):
     def __init__(self, test):
                super().__init__()
                self.test = test

     @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
     async def _extremeAgree(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                self.test.questionExtremelyAgree()
                await self.test.nextQuestion(ctx)


     @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
     async def _kindAgree(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                self.test.questionKindaAgree()
                await self.test.nextQuestion(ctx)

     @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
     async def _neutral(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                self.test.questionNeutral()
                await self.test.nextQuestion(ctx)
        
     @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
     async def _kindaDisagree(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                self.test.questionKindaDisagree()
                await self.test.nextQuestion(ctx)

     @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
     async def _extremeDisagree(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                self.test.questionExtremelyDisagree()
                await self.test.nextQuestion(ctx)


class Mbtitest:
    def __init__(self):
        self.message = None
        self.thread = None
        self.longnames = {
            "E": "Extraverted",
            "I": "Introverted",
            "N": "Intuition",
            "S": "Sensing",
            "F": "Feeling",
            "T": "Thinking",
            "P": "Percieving",
            "J": "Judging"
        }

        self.stats = {
            "E": 0, 
            "I": 0, 
            "N": 0, 
            "S": 0, 
            "T": 0, 
            "F": 0, 
            "P": 0, 
            "J": 0 
        }
        
        self.currentquestion = 0
        self.iestatus = None
        self.snstatus = None
        self.tfstatus = None
        self.pjstatus = None
        self.funfact = None
        self.famousfiction = None
        self.famoustype = None
        self.questions = [
            {
                "question": "I prefer to be around others usually.",
                "yes": "E",
                "no": "I"
                
            },
            {
                "question": "I get more energy from my close friends than other people.",
                "yes": "I",
                "no": "E"
            },
            {
                "question": "I always love when I'm the center of attention.",
                "yes": "E",
                "no": "I"
                
            },
            {
                "question": "I get anxious and overwhelmed if I'm in a crowd of people for long enough.",
                "yes": "I",
                "no": "E"
                
            },
            {
                "question": "I am quite popular in my respective social group.",
                "yes": "E",
                "no": "I"
            },
            {
                "question": "I like to participate in sports.",
                "yes": "S",
                "no": "N"
                
            },
            {
                "question": "I'm always thinking about other things when I do things.",
                "yes": "N",
                "no": "S"
            },
            {
                "question": "I'm able to think quickly in intense situations.",
                "yes": "S",
                "no": "N"
            },
            {
                "question": "I like to make up stories and realities in my head.",
                "yes": "N",
                "no": "S"
            },
            {
                "question": "I like to come up with a lot of ideas.",
                "yes": "N",
                "no": "S"
            },
            {
                "question": "I am good at puzzles.",
                "yes": "T",
                "no": "F"
            },
            {
                "question": "My emotions control me more than I control them.",
                "yes": "F",
                "no": "T"
            },
            {
                "question": "I tend to feel insecure/depressed often.",
                "yes": "F",
                "no": "T"
            },
            {
                "question": "I like to focus on science and the facts rather than my own beliefs.",
                "yes": "T",
                "no": "F"
            },
            {
                "question": "I like solutions that are efficient rather then ones that make people happy.",
                "yes": "T",
                "no": "F"
            },
            {
                "question": "I like to make a lot of backup plans to make sure there's a way for everything.",
                "yes": "J",
                "no": "P"
                
            },
            {
                "question": "I like to just do whatever I feel like doing instead of having a schedule.",
                "yes": "P",
                "no": "J"
               
            },
            {
                "question": "I am always organized with access to everything.",
                "yes": "J",
                "no": "P"
            },
            {
                "question": "I get distracted very easily.",
                "yes": "P",
                "no": "J"
            },
            {
                "question": "I always want extra credit in things and go beyond what's expected of me.",
                "yes": "J",
                "no": "P"
            }
        ]
        self.question = self.questions[self.currentquestion]

    async def start(self, ctx: discord.context.ApplicationContext):
                await ctx.respond("Test Created!")
                self.message = await ctx.channel.send("Please continue in this thread.")
                self.thread = await self.message.create_thread(name="{}'s MBTI test".format(ctx.author.name))
                await self.nextQuestion(ctx, advance=False)

    async def showResults(self, ctx: discord.context.ApplicationContext):
     print("Show Results has been called")

     if self.stats["I"] >= self.stats["E"]:
          self.iestatus = "I"
     else:
          self.iestatus = "E"

     if self.stats["S"] >= self.stats["N"]:
          self.snstatus = "S"
     else:
          self.snstatus = "N"

     if self.stats["T"] >= self.stats["F"]:
          self.tfstatus = "T"
     else:
          self.tfstatus = "F"

     if self.stats["P"] >= self.stats["J"]:
          self.pjstatus = "P"
     else:
          self.pjstatus = "J"

     
     if self.iestatus == "I" and self.snstatus == "N" and self.tfstatus == "T" and self.pjstatus == "J":
         self.funfact = "INTJ is the most introverted type, and is great with coming up with plans!"
         self.famoustype = "Christopher Nolan and Michelle Obama"
         self.famousfiction = "Emperor Palpatine and Giorno Giovanna"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/intj-architect.png"
         self.stack = "Ni-Te-Fi-Se"

     if self.iestatus == "E" and self.snstatus == "N" and self.tfstatus == "T" and self.pjstatus == "J":
         self.funfact = "ENTJ is great with planning, and are most likely to be leaders."
         self.famoustype = "Steve Jobs and Gordon Ramsey"
         self.famousfiction = "Funny Valentine and Ultron"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/entj-commander.png"
         self.stack = "Te-Ni-Se-Fi"

     if self.iestatus == "I" and self.snstatus == "N" and self.tfstatus == "T" and self.pjstatus == "P":
         self.funfact = "INTP are the most intelligent type and are likely to be scientists!"
         self.famoustype = "Einstein and Bill Gates"
         self.famousfiction = "Yoda and L (from death note)"
         self.stack = "Ti-Ne-Si-Fe"

     if self.iestatus == "E" and self.snstatus == "N" and self.tfstatus == "T" and self.pjstatus == "P":
         self.funfact = "ENTP is great at debating, and are likely to push their ideas very strongly!"
         self.famoustype = "Weird Al and Adam Savage"
         self.famousfiction = "Joker and Iron Man"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/entp-debater.png"
         self.stack = "Ne-Ti-Fe-Si"

     if self.iestatus == "I" and self.snstatus == "N" and self.tfstatus == "F" and self.pjstatus == "J":
         self.funfact = "INFJ are the most intuitive type and are the most extroverted introverts! They tend to be very spiritual."
         self.famoustype = "Lady Gaga and Martin Luther King"
         self.famousfiction = "Enrico Pucci and Deku"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/infj-advocate.png"
         self.stack = "Ni-Fe-Ti-Se"

     if self.iestatus == "I" and self.snstatus == "N" and self.tfstatus == "F" and self.pjstatus == "P":
         self.funfact = "INFP are the most popular type for fictional main characters!"
         self.famoustype = "JRR Tolkien and Shakespeare"
         self.famousfiction = "Luke Skywalker and Will Byers"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/infp-mediator.png"
         self.stack = "Fi-Ne-Si-Te"

     if self.iestatus == "E" and self.snstatus == "N" and self.tfstatus == "F" and self.pjstatus == "J":
         self.funfact = "ENFJ are very good and charismatic leaders!"
         self.famoustype = "Obama and Oprah Winfrey"
         self.famousfiction = "Mike Wheeler and Homelander"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/enfj-protagonist.png"
         self.stack = "Fe-Ni-Se-Ti"
         

     if self.iestatus == "E" and self.snstatus == "N" and self.tfstatus == "F" and self.pjstatus == "P":
         self.funfact = "ENFPs are great at spreading their passions, and are the most introverted extroverts!"
         self.famoustype = "Robin Williams and Quentin Tarantino"
         self.famousfiction = "Michael Scott and Joyce Byers"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/enfp-campaigner.png"
         self.stack = "Ne-Fi-Te-Si"

     if self.iestatus == "I" and self.snstatus == "S" and self.tfstatus == "T" and self.pjstatus == "J":
         self.funfact = "ISTJs are very funny, and are very reliable!"
         self.famoustype = "Sting and Natalie Portman"
         self.famousfiction = "Hermoine Granger and Sheldon Cooper"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/istj-logistician.png"
         self.stack = "Si-Te-Fi-Ne"

     if self.iestatus == "I" and self.snstatus == "S" and self.tfstatus == "F" and self.pjstatus == "J":
         self.funfact = "ISFJs are very loving and caring for their loved ones, and are very generous!"
         self.famoustype = "Vin Diesel and Beyonce"
         self.famousfiction = "Captain America and Marge Simpson"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/isfj-defender.png"
         self.stack = "Si-Fe-Ti-Ne"
        

     if self.iestatus == "E" and self.snstatus == "S" and self.tfstatus == "T" and self.pjstatus == "J":
         self.funfact = "ESTJs are great at managing others and care about making a difference!"
         self.famoustype = "Judge Judy and Rockefeller"
         self.famousfiction = "Franziska von Karma and Mr. Krabs"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/estj-executive.png"
         self.stack = "Te-Si-Ne-Fi"

     if self.iestatus == "E" and self.snstatus == "S" and self.tfstatus == "F" and self.pjstatus == "J":
         self.funfact = "ESFJs are very caring and eager to help!"
         self.famoustype = "Taylor Swift and Steve Harvey"
         self.famousfiction = "Dorothy Gale and Woody"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/esfj-consul.png"
         self.stack = "Fe-Si-Ne-Ti"

     if self.iestatus == "I" and self.snstatus == "S" and self.tfstatus == "T" and self.pjstatus == "P":
         self.funfact = "ISTPs are creative builders who love a hands-on experience with anything!"
         self.famoustype = "Harrison Ford and Michael Jordan"
         self.famousfiction = "Jotaro Kujo and Indiana Jones"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/istp-virtuoso.png"
         self.stack = "Ti-Se-Ni-Fe"

     if self.iestatus == "I" and self.snstatus == "S" and self.tfstatus == "F" and self.pjstatus == "P":
         self.funfact = "ISFPs are creative and expressive, and usually are artists!"
         self.famoustype = "Kevin Costner and Jungkook"
         self.famousfiction = "Jesse Pinkman and Eleven"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/isfp-adventurer.png"
         self.stack = "Fi-Se-Ni-Te"

     if self.iestatus == "E" and self.snstatus == "S" and self.tfstatus == "T" and self.pjstatus == "P":
         self.funfact = "ESTPs are the most extroverted type and are very adventerous!"
         self.famoustype = "Ernest Hemingway and Eddie Murphy"
         self.famousfiction = "Sonic the Hedgehog and Joseph Joestar"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/estp-entrepreneur.png"
         self.stack = "Se-Ti-Fe-Ni"

     if self.iestatus == "E" and self.snstatus == "S" and self.tfstatus == "F" and self.pjstatus == "P":
         self.funfact = "ESFPs are the most energetic personality, and are the most emotional!"
         self.famoustype = "Elton John and Adele"
         self.famousfiction = "Homer Simpson and Peter Griffin"
         iconp = "https://www.16personalities.com/static/images/personality-types/avatars/esfp-entertainer.png"
         self.stack = "Se-Fi-Te-Ni"
     mbtilist = list("{0}{1}{2}{3}".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus))
     print(mbtilist)
     embed = discord.Embed(
        title="Your MBTI: {0}{1}{2}{3}".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus),
        description="""
         _{0}, {1}, {2}, and {3}_

         **Scores:**
         Introverted (I) Score: {4}
         Extraverted (E) Score: {5}
         Sensing (S) Score: {6}
         Intuition (N) Score: {7}
         Thinking (T) Score: {8}
         Feeling (F) Score: {9}
         Percieving (P) Score: {10}
         Judging (J) Score: {11}
         """.format(self.longnames[self.iestatus], self.longnames[self.snstatus], self.longnames[self.tfstatus], self.longnames[self.pjstatus], str(self.stats["I"]), str(self.stats["E"]), str(self.stats["S"]), str(self.stats["N"]), str(self.stats["T"]), str(self.stats["F"]), str(self.stats["P"]), str(self.stats["J"])),
        color=discord.Colour.red()
     )

     embed.add_field(name="Fun Fact about {0}{1}{2}{3}s:".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus), value=self.funfact)
     embed.add_field(name="Famous {0}{1}{2}{3}s:".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus), value=self.famoustype)
     embed.add_field(name="Famous Fictional {0}{1}{2}{3}s:".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus), value=self.famousfiction)
     embed.add_field(name="Function Stack", value=self.stack)
     embed.set_footer(text="For the most acurrate typing, also take the /cogfunctest!")
     view = discord.ui.View()
     b = discord.ui.Button(label="Learn more about {0}{1}{2}{3}".format(self.iestatus, self.snstatus, self.tfstatus, self.pjstatus), style=discord.ButtonStyle.link, url="https://www.truity.com/blog/personality-type/{0}{1}{2}{3}".format(self.iestatus.lower(), self.snstatus.lower(), self.tfstatus.lower(), self.pjstatus.lower()))
     view.add_item(b)
     await self.thread.send(embed=embed, view=view)

    

    def questionExtremelyAgree(self):
        self.stats[self.questions[self.currentquestion]["yes"]] += 2

    def questionKindaAgree(self):
        self.stats[self.questions[self.currentquestion]["yes"]] += 1.5

    def questionNeutral(self):
        self.stats[self.questions[self.currentquestion]["yes"]] += 1
        self.stats[self.questions[self.currentquestion]["no"]] += 1

    def questionKindaDisagree(self):
        self.stats[self.questions[self.currentquestion]["no"]] += 1.5

    def questionExtremelyDisagree(self):
        self.stats[self.questions[self.currentquestion]["no"]] += 2

    async def nextQuestion(self, ctx: discord.context.ApplicationContext, advance=True):
         if advance:
            self.currentquestion += 1
         if self.currentquestion >= 19:
            await self.showResults(ctx)
            return
         self.question = self.questions[self.currentquestion]

         await self.thread.send("{0}: {1}".format(self.currentquestion + 1, self.question["question"]), view=QuestionView(self))
         

    











class Mbtitestcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="mbtitest", description="Do a test to figure out your MBTI personality type!")
    async def enneagramtestcmd(self, ctx):
          e = Mbtitest()
          await e.start(ctx)











def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Mbtitestcmd(bot)) # add the cog to the bot
