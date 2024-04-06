#    UltraBot Discord Bot
#    Copyright (C) 2024  Holden Latta

#    UltraBot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    UltraBot is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with UltraBot.  If not, see <https://www.gnu.org/licenses/>.

import discord
from discord.ext import commands
import logging

class EssentialsCog(discord.Cog):
    def __init__(self, bot: commands.Bot):
        logging.info("EssentialsCog has been initalized!")
        self.bot = bot
    
    @commands.slash_command(name="ping", description="Sends the bot's ping or latency")
    async def ping(self, interaction):
        latency = round(self.bot.latency*100, 2)
        await interaction.response.send_message(f"Pong! Latency or ping is {latency}")

    @commands.slash_command(name="helloworld", description="If your program can't say this, don't talk to me")
    async def helloworld(self, interaction):
        await interaction.response.send_message(":earth_americas: Hello, World!")

