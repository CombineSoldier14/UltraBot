import discord
from discord.ext import commands
import os
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION
import cogs.lists
from cogs.lists import mbtilist



class TiViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tiscore = 2
                await self.test.question2(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tiscore = 1.5
                await self.test.question2(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tiscore = 1
                await self.test.question2(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tiscore = 0.5
                await self.test.question2(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tiscore = 0
                await self.test.question2(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class TiViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tiscore += 2
                await self.test.question3(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tiscore += 1.5
                await self.test.question3(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tiscore += 1
                await self.test.question3(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tiscore += .5
                await self.test.question3(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tiscore 
                await self.test.question3(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
class TiViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tiscore += 2
                await self.test.question4(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tiscore += 1.5
                await self.test.question4(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tiscore += 1
                await self.test.question4(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tiscore += .5
                await self.test.question4(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tiscore 
                await self.test.question4(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
class TeViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tescore = 2
                await self.test.question5(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tescore = 1.5
                await self.test.question5(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tescore += 1
                await self.test.question5(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tescore = 0.5
                await self.test.question5(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tescore = 0
                await self.test.question5(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class TeViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tescore += 2
                await self.test.question6(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tescore += 1.5
                await self.test.question6(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tescore += 1
                await self.test.question6(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tescore += .5
                await self.test.question6(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tescore 
                await self.test.question6(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class TeViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.tescore += 2
                await self.test.question7(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.tescore += 1.5
                await self.test.question7(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.tescore += 1
                await self.test.question7(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.tescore += .5
                await self.test.question7(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.tescore 
                await self.test.question7(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NiViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.niscore += 2
                await self.test.question8(interaction)(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.niscore += 1.5
                await self.test.question8(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.niscore += 1
                await self.test.question8(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.niscore += .5
                await self.test.question8(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.niscore 
                await self.test.question8(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NiViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.niscore += 2
                await self.test.question9(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.niscore += 1.5
                await self.test.question9(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.niscore += 1
                await self.test.question9(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.niscore += .5
                await self.test.question9(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.niscore 
                await self.test.question9(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NiViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.niscore += 2
                await self.test.question10(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.niscore += 1.5
                await self.test.question10(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.niscore += 1
                await self.test.question10(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.niscore += .5
                await self.test.question10(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.niscore 
                await self.test.question10(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NeViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.nescore += 2
                await self.test.question11(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.nescore += 1.5
                await self.test.question11(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.nescore += 1
                await self.test.question11(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.nescore += .5
                await self.test.question11(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.nescore 
                await self.test.question11(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NeViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.nescore += 2
                await self.test.question12(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.nescore += 1.5
                await self.test.question12(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.nescore += 1
                await self.test.question12(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.nescore += .5
                await self.test.question12(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.nescore 
                await self.test.question12(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class NeViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.nescore += 2
                await self.test.question13(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.nescore += 1.5
                await self.test.question13(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.nescore += 1
                await self.test.question13(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.nescore += .5
                await self.test.question13(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.nescore 
                await self.test.question13(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SiViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.siscore += 2
                await self.test.question14(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.siscore += 1.5
                await self.test.question14(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.siscore += 1
                await self.test.question14(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.siscore += .5
                await self.test.question14(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.siscore 
                await self.test.question14(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SiViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.siscore += 2
                await self.test.question15(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.siscore += 1.5
                await self.test.question15(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.siscore += 1
                await self.test.question15(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.siscore += .5
                await self.test.question15(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.siscore 
                await self.test.question15(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SiViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.siscore += 2
                await self.test.question16(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.siscore += 1.5
                await self.test.question16(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.siscore += 1
                await self.test.question16(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.siscore += .5
                await self.test.question16(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.siscore 
                await self.test.question16(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SeViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.sescore += 2
                await self.test.question17(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.sescore += 1.5
                await self.test.question17(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.sescore += 1
                await self.test.question17(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.sescore += .5
                await self.test.question17(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.sescore 
                await self.test.question17(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SeViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.sescore += 2
                await self.test.question18(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.sescore += 1.5
                await self.test.question18(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.sescore += 1
                await self.test.question18(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.sescore += .5
                await self.test.question18(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.sescore 
                await self.test.question18(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class SeViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.sescore += 2
                await self.test.question19(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.sescore += 1.5
                await self.test.question19(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.sescore += 1
                await self.test.question19(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.sescore += .5
                await self.test.question19(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.sescore 
                await self.test.question19(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class FiViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fiscore += 2
                await self.test.question20(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fiscore += 1.5
                await self.test.question20(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fiscore += 1
                await self.test.question20(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fiscore += .5
                await self.test.question20(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fiscore 
                await self.test.question20(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class FiViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fiscore += 2
                await self.test.question21(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fiscore += 1.5
                await self.test.question21(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fiscore += 1
                await self.test.question21(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fiscore += .5
                await self.test.question21(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fiscore 
                await self.test.question21(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
class FiViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fiscore += 2
                await self.test.question22(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fiscore += 1.5
                await self.test.question22(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fiscore += 1
                await self.test.question22(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fiscore += .5
                await self.test.question22(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fiscore 
                await self.test.question22(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
class FeViewOne(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fescore += 2
                await self.test.question23(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fescore += 1.5
                await self.test.question23(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fescore += 1
                await self.test.question23(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fescore += .5
                await self.test.question23(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fescore 
                await self.test.question23(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        

class FeViewTwo(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fescore += 2
                await self.test.question24(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fescore += 1.5
                await self.test.question24(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fescore += 1
                await self.test.question24(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fescore += .5
                await self.test.question24(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fescore 
                await self.test.question24(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

class FeViewThree(discord.ui.View):
        def __init__(self, test):
                super().__init__()
                self.test = test

        @discord.ui.button(label="Extremely Agree", style=discord.ButtonStyle.green)
        async def _extremeAgree(self, button, interaction):
                self.test.fescore += 2
                await self.test.finish(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return


        @discord.ui.button(label="Kinda Agree", style=discord.ButtonStyle.green)
        async def _kindAgree(self, button, interaction):
                self.test.fescore += 1.5
                await self.test.finish(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Neutral", style=discord.ButtonStyle.gray)
        async def _neutral(self, button, interaction):
                self.test.fescore += 1
                await self.test.finish(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return
        
        @discord.ui.button(label="Kinda Disagree", style=discord.ButtonStyle.red)
        async def _kindaDisagree(self, button, interaction):
                self.test.fescore += .5
                await self.test.finish(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return

        @discord.ui.button(label="Extremely Disagree", style=discord.ButtonStyle.red)
        async def _extremeDisagree(self, button, interaction):
                self.test.fescore 
                await self.test.finish(interaction)
                self.disable_all_items()
                await interaction.response.edit_message(view=self)
                return



class Test():
        def __init__(self):
                self.thread = 0
                self.tiscore = 0
                self.tescore = 0
                self.niscore = 0
                self.nescore = 0
                self.siscore = 0
                self.sescore = 0
                self.fiscore = 0
                self.fescore = 0
                self.questions = [
                                  #Ti Questions
                                  "You have an internal logical system for thinking that gets revised as you learn new things", 
                                  "You develop your own methods and strategies for problem solving",
                                  "You are open to new insights and perspectives to perfect an idea",

                                  #Te Questions
                                  "Making sure people have the resources they need to succeed is very important to you.",
                                  "You like to rely on ONLY the facts and data when making a decision",
                                  "You are very results-oriented",

                                  #Ni Questions (thanks Alex!)
                                  "You are focused on a single conclusion, goal or vision",
                                  "You are future oriented",
                                  "You tend to have an \"aha\" moment where the solution seems to pop into your head",

                                  #Ne Questions
                                  "You are extremely interested in how the world works more than anything else.",
                                  "You tend to come up with a lot more ideas than most",
                                  "You are constantly focused on the various possibilities of the world",

                                  #Si Questions
                                  "Sensory and vividness plays a big role in how you recall memories",
                                  "Tradition is very important to you",
                                  "You use past experiences to understand the present",

                                  #Se Questions (thanks Alex!)
                                  "You seek sensory experience such as thrill or eating tasty food to get a physical response",
                                  "You are unlikely to miss something in your surroundings",
                                  "You live in the moment, not the past, not the future",

                                  #Fi Questions (thanks Alex!)
                                  "You make decisions based on what your believe to be morally correct or incorrect",
                                  "You are very in tune with your emotions and can tell what each feeling means",
                                  "You value being authentic to who you are",

                                  #Fe Questions (thanks Alex!)
                                  "You are very mindful of others needs and emotions in decision making",
                                  "You tend to sacrifice your own needs and desires for others",
                                  "You respect social and cultural norms",
                                  ]
                
        
                
                
        async def start(self, interaction: discord.Interaction):
                await interaction.response.send_message("Test Created!")
                message = await interaction.channel.send("Please continue in this thread.")
                self.thread = await message.create_thread(name="{}'s MBTI test".format(interaction.author.name))
                await self.thread.send("1/24: {0}".format(self.questions[0]), view=TiViewOne(self))
        
        async def question2(self, interaction):
                await self.thread.send("2/24: {0}".format(self.questions[1]), view=TiViewTwo(self))
                

        async def question3(self, interaction):
                await self.thread.send("3/24: {0}".format(self.questions[2]), view=TiViewThree(self))
                

        async def question4(self, interaction):
                await self.thread.send("4/24: {0}".format(self.questions[3]), view=TeViewOne(self))

        async def question5(self, interaction):
                await self.thread.send("5/24: {0}".format(self.questions[4]), view=TeViewTwo(self))

        async def question6(self, interaction):
                await self.thread.send("6/24: {0}".format(self.questions[5]), view=TeViewThree(self))

        async def question7(self, interaction):
                await self.thread.send("7/24: {0}".format(self.questions[6]), view=NiViewOne(self))

        async def question8(self, interaction):
                await self.thread.send("8/24: {0}".format(self.questions[7]), view=NiViewTwo(self))

        async def question9(self, interaction):
                await self.thread.send("9/24: {0}".format(self.questions[8]), view=NiViewThree(self))

        async def question10(self, interaction):
                await self.thread.send("10/24: {0}".format(self.questions[9]), view=NeViewOne(self))

        async def question11(self, interaction):
                await self.thread.send("11/24: {0}".format(self.questions[10]), view=NeViewTwo(self))

        async def question12(self, interaction):
                await self.thread.send("12/24: {0}".format(self.questions[11]), view=NeViewThree(self))

        async def question13(self, interaction):
                await self.thread.send("13/24: {0}".format(self.questions[12]), view=SiViewOne(self))

        async def question14(self, interaction):
                await self.thread.send("14/24: {0}".format(self.questions[13]), view=SiViewTwo(self))

        async def question15(self, interaction):
                await self.thread.send("15/24: {0}".format(self.questions[14]), view=SiViewThree(self))

        async def question16(self, interaction):
                await self.thread.send("16/24: {0}".format(self.questions[15]), view=SeViewOne(self))

        async def question17(self, interaction):
                await self.thread.send("17/24: {0}".format(self.questions[16]), view=SeViewTwo(self))

        async def question18(self, interaction):
                await self.thread.send("18/24: {0}".format(self.questions[17]), view=SeViewThree(self))

        async def question19(self, interaction):
                await self.thread.send("19/24: {0}".format(self.questions[18]), view=FiViewOne(self))

        async def question20(self, interaction):
                await self.thread.send("20/24: {0}".format(self.questions[19]), view=FiViewTwo(self))

        async def question21(self, interaction):
                await self.thread.send("21/24: {0}".format(self.questions[20]), view=FiViewThree(self))

        async def question22(self, interaction):
                await self.thread.send("22/24: {0}".format(self.questions[21]), view=FeViewOne(self))

        async def question23(self, interaction):
                await self.thread.send("23/24: {0}".format(self.questions[22]), view=FeViewTwo(self))

        async def question24(self, interaction):
                await self.thread.send("24/24: {0}".format(self.questions[23]), view=FeViewThree(self))

        async def finish(self, interaction):
                embed = cogs.combinebot.makeEmbed(
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

                    """.format(self.tiscore * 10, self.tescore * 10, self.niscore * 10, self.nescore * 10, self.siscore * 10, self.sescore * 10, self.fiscore * 10, self.fescore * 10),
                    color=discord.Colour.blurple()
                )
                embed.add_field(name="Create your Stack", value="To create your stack, take your top two highest functions (referred to in this case as Dominant and Secondary) and put them into **/mbtifinder** to get your MBTI and full stack! (NOTE: There is some criteria involved with this. Your top two functions must be one introverted and one extraverted. They also cannot be opposites, so no Ti-Fe. If this doens't work for your results then simply take the third highest or beyond.)")
                await self.thread.send(embed=embed)

    

        
        
                
                


class Cogfunctest(commands.Cog):
    group = discord.SlashCommandGroup(name="dev", description="Commands for development/testing purposes")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="cogfunctest", description="Test to see your results on your MBTI cognitive functions!")
    async def cogfuncoop(self, interaction):
            t = Test()
            await t.start(interaction)










def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Cogfunctest(bot)) # add the cog to the bot

