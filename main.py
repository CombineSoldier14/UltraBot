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
import json

# -- Cog imports --
import ultrabot.essentials

# Defing bot and bot user intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print("UltraBot.py is up and running!")
    bot.auto_sync_commands = True

# say is intentionally not a slash command.
#Don't worry, the french people joke is an inside joke with my friend
@bot.command(name="say")
async def _say(ctx, text):
    
    await ctx.send(text)
    await ctx.message.delete()

# ADD COMMAND COGS
# ----------
bot.add_cog(ultrabot.essentials.EssentialsCog(bot))
# ----------

# AutoRun prevention with __name__
if __name__ == "__main__":
    with open("token.json", "r") as f:
      _d = json.load(f)
    bot.run(_d["BOT_TOKEN"])
