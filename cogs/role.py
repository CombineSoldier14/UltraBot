import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json


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


class Role(commands.Cog):
    group = discord.SlashCommandGroup(name="role", description="Commands for managing roles")

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None





    @group.command(name="addrole", description="Adds a role to a user.")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Option(discord.Member, description="User to give role to", required=True), role: discord.Option(discord.Role, description="Role to give user", required=True)):
       await user.add_roles(role, atomic=True)
       await ctx.respond("The role has been added to the user!")

    @group.command(name="removerole", description="Removes a role from a user.")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Option(discord.Member, description="User to remove role from", required=True), role: discord.Option(discord.Role, description="Role to remove", required=True)):
       await user.remove_roles(role, atomic=True)
       await ctx.respond("The role has been removed from the user!")

    @group.command(name="createrole", description="Creates a basic no perms role.")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, name: discord.Option(str, description="Name of role", required=True), server: discord.Option(discord.Guild, description="Name of the server to make role in. Case sensitive!", required=True)):
       await server.create_role(name=name)
       await ctx.respond("The role **" + name + "** has been created.")

    @group.command(name="roleinfo", description="Gets detailed info on a role")
    async def roleinfo(self, ctx, role: discord.Option(discord.Role, description="Role to get info on")):
         embed = discord.Embed(
              title = "Info on {0}".format(role.name),
              description = """
              **Created at:** {0} 
              **Hoisted:** {1} 
              **Mentionable:** {2}
              **Position:** {3} 
              
              
              """.format(role.created_at, role.hoist, role.mentionable, str(role.position)),
              color = role.colour,
         
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         
         await ctx.respond(embed=embed)



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Role(bot)) # add the cog to the bot
