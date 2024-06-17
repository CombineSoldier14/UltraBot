import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION



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
                await self.test.nextQuestion(ctx)


class Enneagramtest:
    def __init__(self):
        self.message = None
        self.thread = None
        self.longnames = {
            1: "Type 1",
            2: "Type 2",
            3: "Type 3",
            5: "Type 4",
            5: "Type 5",
            6: "Type 6",
            7: "Type 7",
            8: "Type 8",
            9: "Type 9"
        }

        self.stats = {
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0, 
            7: 0, 
            8: 0,
            9: 0 
        }
        
        self.currentquestion = 0
        self.type = None
        self.wing = None
        self.wings = None
        self.wing1 = None
        self.wing2 = None
        self.diction = None
        self.questions = [
            {
                "question": "You have a strong sense of right and wrong.",
                "type": 1
                
            },
            {
                "question": "You heavily care about improving the world around you.",
                "type": 1
                
            },
            {
                "question": "You want to be useful.",
                "type": 1
                
            },
            {
                "question": "You feel the need often to justify your actions.",
                "type": 1
                
            },
            {
                "question": "You have a set of principles that must be followed at all times.",
                "type": 1
                
            },
            {
                "question": "I always put others first.",
                "type": 2
                
            },
            {
                "question": "I try my best to please those around me.",
                "type": 2
                
            },
            {
                "question": "I want to help people a lot",
                "type": 2
                
            },
            {
                "question": "The best thing is to put other people's needs first.",
                "type": 2
                
            },
            {
                "question": "You love unconditionally.",
                "type": 2
                
            },
            {
                "question": "You are goal oriented.",
                "type": 3
                
            },
            {
                "question": "You exhibit charisma and charm onto others.",
                "type": 3
                
            },
            {
                "question": "To be seen as a loser would be the worst thing for you.",
                "type": 3
                
            },
            {
                "question": "You are VERY competitive.",
                "type": 3
            
            },
            {
                "question": "You want to be noticed through success.",
                "type": 3
                
            },
            {
                "question": "My self-image is very important to me.",
                "type": 4
                
            },
            {
                "question": "I like to look at myself as different from other people.",
                "type": 4
                
            },
            {
                "question": "You base your identity on emotional reactions.",
                "type": 4
                
            },
            {
                "question": "When not stressed, you like to be honest to yourself.",
                "type": 4
               
            },
            {
                "question": "You always feel like you're missing something in life.",
                "type": 4
                
            },
            {
                "question": "You focus heavily on understanding complex ideas and skills.",
                "type": 5
                
            },
            {
                "question": "You have specialized skill sets for your expertise.",
                "type": 5
                
            },
            {
                "question": "You want to understand how the world works more than anything.",
                "type": 5
                
            },
            {
                "question": "You want to acquire as much knowledge as possible to understand something.",
                "type": 5,
                
            },
            {
                "question": "You are scared of not being able to do things as well as others.",
                "type": 5,
                
            },
            {
                "question": "You are very loyal to your friends and beliefs.",
                "type": 6,
                
            },
            {

                "question": "You need guidance and help in life.",
                "type": 6,
                
            },
            {

                "question": "You believe that all authority must be questioned.",
                "type": 6,
                
            },
            {

                "question": "You get very anxious when doing a big thing on your own.",
                "type": 6,
                
            },
            {

                "question": "You are easily influenced by others.",
                "type": 6,
                
            },
            {

                "question": "You like working on a multitude of projects at the same time.",
                "type": 7,
                
            },
            {

                "question": "You enjoy intellecually-stimulating activities.",
                "type": 7,
                
            },
            {

                "question": "You are good at brainstorming.",
                "type": 7,
                
            },
            {

                "question": "You have trouble listening to people.",
                "type": 7,
                
            },
            {

                "question": "You fear boredom.",
                "type": 7,
                
            },
            {

                "question": "You desire being in control of your life more than anything else.",
                "type": 8,
                
            },
            {

                "question": "You like improving yourself with challenges.",
                "type": 8,
                
            },
            {

                "question": "You don't care much about what other people think of you.",
                "type": 8,
                
            },
            {

                "question": "You don't like showing weakness to others.",
                "type": 8,
                
            },
            {

                "question": "You have a lot of determination and willpower.",
                "type": 8,
                
            },
            {

                "question": "You are spiritual.",
                "type": 9,
                
            },
            {

                "question": "You greatly value deep connections with others.",
                "type": 9,
                
            },
            {

                "question": "You try to keep the peace between others.",
                "type": 9,
                
            },
            {

                "question": "You would give up your own needs to benefit others.",
                "type": 9,
                
            },
            {

                "question": "You value other perspectives on things.",
                "type": 9,
                
            },
        ]
        self.question = self.questions[self.currentquestion]

    async def start(self, ctx: discord.context.ApplicationContext):
                await ctx.respond("Test Created!")
                self.message = await ctx.channel.send("Please continue in this thread.")
                self.thread = await self.message.create_thread(name="{}'s Enneagram test".format(ctx.author.name))
                await self.nextQuestion(ctx, advance=False)

    async def showResults(self, ctx: discord.context.ApplicationContext):
        self.stats[1] += 0.1
        self.stats[2] += 0.2
        self.stats[3] += 0.3
        self.stats[4] += 0.4
        self.stats[5] += 0.5
        self.stats[6] += 0.6
        self.stats[7] += 0.7
        self.stats[8] += 0.8
        self.stats[9] += 0.9
        self.diction = {self.stats[1]:1, self.stats[2]:2, self.stats[3]:3, self.stats[4]:4, self.stats[5]:5, self.stats[6]:6, self.stats[7]:7, self.stats[8]:8, self.stats[9]:9}
        self.type = self.diction[max(self.stats[1], self.stats[2], self.stats[3], self.stats[4], self.stats[5], self.stats[6], self.stats[7], self.stats[8], self.stats[9])]
        if self.type == 1:
            self.wing = self.diction[max(self.stats[2], self.stats[9])]
        elif self.type == 9:
            self.wing = self.diction[max(self.stats[8], self.stats[1])]
        else:
            self.wing = self.diction[max(self.stats[self.type - 1], self.stats[self.type + 1])]
        embed=cogs.combinebot.makeEmbed(
              title="Your Enneagram Test Results",
              description="""
Type 1 Score: **{0}**
Type 2 Score: **{1}**
Type 3 Score: **{2}**
Type 4 Score: **{3}**
Type 5 Score: **{4}**
Type 6 Score: **{5}**
Type 7 Score: **{6}**
Type 8 Score: **{7}**
Type 9 Score: **{8}**

You are most likely a type **{9}**. When taking wings into consideration, you are most likely a **{10}w{11}**.


""".format(self.stats[1] - 0.1, self.stats[2] - 0.2, self.stats[3] - 0.3, self.stats[4]- 0.4, self.stats[5]- 0.5, self.stats[6]- 0.6, self.stats[7]- 0.7, self.stats[8]- 0.8, self.stats[9]- 0.9, str(self.type), str(self.type), str(self.wing)),
            color=discord.Colour.blurple(),
         )
        embed.set_footer(text="To determine your wing, take your highest type and look at the neigboring types (For example, if your highest is 5, you would look at 4 and 6) and which ever is highest is your wing!")
        await self.thread.send(embed=embed)

    

    def questionExtremelyAgree(self):
        self.stats[self.questions[self.currentquestion]["type"]] += 20

    def questionKindaAgree(self):
        self.stats[self.questions[self.currentquestion]["type"]] += 15

    def questionNeutral(self):
        self.stats[self.questions[self.currentquestion]["type"]] += 10

    def questionKindaDisagree(self):
        self.stats[self.questions[self.currentquestion]["type"]] += 5

    async def nextQuestion(self, ctx: discord.context.ApplicationContext, advance=True):
         if advance:
            self.currentquestion += 1
         if self.currentquestion >= len(self.questions):
            await self.showResults(ctx)
            return
         self.question = self.questions[self.currentquestion]

         await self.thread.send("{0}: {1}".format(self.currentquestion + 1, self.question["question"]), view=QuestionView(self))
         

    











class Enneagramtestcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="enneagramtest", description="Do a test to figure out your Enneagram personality type!")
    async def enneagramtestcmd(self, ctx):
          e = Enneagramtest()
          await e.start(ctx)











def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Enneagramtestcmd(bot)) # add the cog to the bot

