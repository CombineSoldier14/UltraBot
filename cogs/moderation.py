import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime
import cogs.combinebot

info = cogs.combinebot.getBotInfo()
name = info[0]["name"]
icon = info[0]["icon"]
VERSION = info[0]["version"]
LATESTADDITION = info[0]["latest_addition"]





class Moderation(commands.Cog):
    group = discord.SlashCommandGroup(name="moderation", description="Commands for server management and moderation")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



    @group.command(name="userid", description="Find the ID of a mentioned user")
    async def userid(self, ctx, user: discord.Option(discord.Member, description="Member to find ID of", required=True)):
      await ctx.respond(f"That user's id is " + str(user.id))

    @group.command(name="ban", description="Bans a user.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Option(discord.Member, description="User to ban", required=True), 
                  reason: discord.Option(str, description="Reason for ban", required=True)):
      await user.ban(reason = reason)
      embed = cogs.combinebot.makeEmbed(
       title="Ban",
       description="The user " + str(user) + " has been banned from the server.",
       color=discord.Colour.red(),
    )
      embed.set_footer(text="Reason: " + reason)

      await ctx.respond(embed=embed)
    
    @group.command(name="kick", description="Kicks a user.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Option(discord.Member, description="User to kick", required=True), 
                  reason: discord.Option(str, description="Reason for ban", required=True)):
      await user.kick(reason = reason)
      embed = cogs.combinebot.makeEmbed(
       title="Kick",
       description="The user " + str(user) + " has been kicked from the server.",
       color=discord.Colour.red(),
    )
      embed.set_footer(text="Reason: " + reason)

      await ctx.respond(embed=embed)

    @group.command(name="poll", description="Creates a votable yes or no poll!")
    @commands.has_permissions(administrator = True)
    async def poll(self, ctx, title: discord.Option(str, description="Title of poll", required=True), description: discord.Option(str, description="Your yes or no poll description", required=True)):
       embed = cogs.combinebot.makeEmbed(
          title=title,
          description=description,
          color=discord.Colour.blurple(),

       )

       
       emoji = '\N{THUMBS UP SIGN}'
       emoji2 = '\N{THUMBS DOWN SIGN}'
       message = await ctx.respond(embed=embed)
       await message.add_reaction(emoji)
       await message.add_reaction(emoji2)
    
    @group.command(name="purge", description="Purges a certain number of messages from a channel")
    @commands.has_permissions(manage_messages = True)
    @commands.has_permissions(read_message_history = True)
    async def purge(self, ctx, number: discord.Option(int, description="Number of messages to purge. Max is 100", required=True)):
       await ctx.channel.purge(limit=number)
       await ctx.respond("**" + str(number) + "** messages have been purged!")


    @group.command(name="timeout", description="Timeout a user.")
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, time: discord.Option(int, description="Amount of minutes to time out user", required=True), user: discord.Option(discord.Member, description="User to timeout", required=True)):
        await user.timeout_for(datetime.timedelta(minutes=time))
        await ctx.respond("{0} has been timed out for **{1}**.".format(user, time))



    @group.command(name="untimeout", description="Removes a timeout from a user.")
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, user: discord.Option(discord.Member, description="User to untimeout", required=True)):
        await user.remove_timeout()
        await ctx.respond("{0} has had their timeout removed!".format(user))


    @group.command(name="createchannel", description="Creates a basic text channel")
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, name: discord.Option(str, description="Name of channel"), guild: discord.Option(discord.Guild, description="Name of server to make channel in. Case sensitive!")):
        await guild.create_text_channel('{0}'.format(name))
        await ctx.respond("The channel **#{0}** has been created!".format(name))

    @group.command(name="createvoicechannel", description="Creates a basic voice channel")
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, name: discord.Option(str, description="Name of channel"), guild: discord.Option(discord.Guild, description="Name of server to make channel in. Case sensitive!")):
        await guild.create_voice_channel('{0}'.format(name))
        await ctx.respond("The channel **#{0}** has been created!".format(name))

    @group.command(name="deletechannel", description="Deletes a channel in the server.")
    @commands.has_permissions(manage_channels=True)
    async def deletechannel(self, ctx, channel: discord.Option(discord.TextChannel, description="Channel to delete"), reason: discord.Option(str, description="Reason for deletion")):
        await channel.delete(reason=reason)
        embed = cogs.combinebot.makeEmbed(
            title="{} was deleted".format(channel),
            description="Reason: {}".format(reason),
            color=discord.Colour.red(),
        )
        await ctx.respond(embed=embed)


    @group.command(name="thread", description="Create a new basic thread")
    @commands.has_permissions(create_public_threads=True)
    async def thread(self, ctx, title: discord.Option(str, description="Title of thread", required=True), startmsg: discord.Option(str, description="Starting message in thread", required=True)):
        message = await ctx.send(startmsg)
        await message.create_thread(name=title)
        await ctx.respond("Your thread, **{0}**, has been created!".format(title))



    

    
       

    @ban.error
    async def ban_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to ban members.")

    @kick.error
    async def kick_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to kick members.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Moderation(bot)) # add the cog to the bot









