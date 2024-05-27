import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import requests
import json
import random
import cogs.requestHandler as handler
from random import uniform

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
            game = "Ace Attorney: Dual Destinies"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"





class Apis(commands.Cog):
    group = discord.SlashCommandGroup(name="api", description="Commands that use online APIs made by other people")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(name="dadjoke", description="Get a random dad joke!")
    async def dadjoke(self, ctx):
        r = handler.get("https://official-joke-api.appspot.com/random_joke")
        j = json.loads(r.text)
        await ctx.respond("{0} {1}".format(j["setup"], j["punchline"]))
    
    @group.command(name="xkcd", description="Get a random XKCD comic!")
    async def xkcd(self, ctx):
        xkcdlink = handler.get("https://xkcd.com/" + str(random.randint(1, 2916)) + "/info.0.json")
        xkcdjson = json.loads(xkcdlink.text)
            
        embed = discord.Embed(
            
            
            title="#" + str(xkcdjson["num"]) + " - " + xkcdjson["title"],
            description=xkcdjson["alt"],
            color=discord.Colour.blurple(),
            
            
        )
        embed.set_image(url=xkcdjson["img"])
        embed.set_footer(text="Year: " + str(xkcdjson["year"]) + ", Month " + str(xkcdjson["month"]) + ", Day " + str(xkcdjson["day"]))
        await ctx.respond(embed=embed)
    
    @group.command(name="dogpics", description="Random picture of a dog!")
    async def dogpics(self, ctx):
        doglink = handler.get("https://dog.ceo/api/breeds/image/random")
        dogjson = json.loads(doglink.text)

        embed = discord.Embed(
            title="Dog",
            color=discord.Colour.blurple(),
        )
        embed.set_image(url=dogjson["message"])
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
        await ctx.respond(embed=embed)
    
    @group.command(name="shakespeare", description="Translate english text to Shakespeare english!")
    async def shakespeare(self, ctx, text: discord.Option(str, description="Text to translate", required=True)):
         rshake = handler.get("https://api.funtranslations.com/translate/shakespeare.json?text={0}".format(text))
         jshake = json.loads(rshake.text)

         embed = discord.Embed(
              title = jshake["contents"]["translated"],
              description = jshake["contents"]["text"],
              color = discord.Colour.orange(),
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_thumbnail(url="https://hips.hearstapps.com/hmg-prod/images/william-shakespeare-194895-1-402.jpg")
         await ctx.respond(embed=embed)


    @group.command(name="jojostand", description="Get a random jojo stand and its info!")
    async def jojostand(self, ctx):
         id = random.randint(1, 155)
         rstand = handler.get("https://stand-by-me.herokuapp.com/api/v1/stands/{0}".format(str(id)))
         jstand = json.loads(rstand.text)

         embed = discord.Embed(
              title=jstand["name"],
              description="""
              **Alternate name:** {0}
              **Japanese name:** {1}
              **Chapter:** {2}
              **Abilities:** {3}
              **Battle Cry:** {4}

               """.format(jstand["alternateName"], jstand["japaneseName"], jstand["chapter"], jstand["abilities"], jstand["battlecry"]),
               color=discord.Colour.blurple()
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jstand["image"]))

         await ctx.respond(embed=embed)


    @group.command(name="jojocharacter", description="Get a random jojo character and their info!")
    async def jojocharacter(self, ctx):
         ctx.defer()
         id = random.randint(1, 175)
         rchar = handler.get("https://stand-by-me.herokuapp.com/api/v1/characters/{0}".format(str(id)))
         jchar = json.loads(rchar.text)

         embed = discord.Embed(
              title=jchar["name"],
              description="""
              **Japanese name:** {0}
              **Abilities:** {1}
              **Nationality:** {2}
              **Catchphrase:** {3}
              **Family:** {4}
              **Chapter:** {5}
              **Still alive?** ||{6}||
              **Is human?** {7}

               """.format(jchar["japaneseName"], 
                          jchar["abilities"], 
                          jchar["nationality"], 
                          jchar["catchphrase"], 
                          jchar["family"], 
                          jchar["chapter"], 
                          ("yes" if jchar["living"] else "no"),
                          jchar["isHuman"]),
               color=discord.Colour.blurple(),
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jchar["image"]))
         await ctx.respond(embed=embed)
         
    @group.command(name="meme", description="Get a random meme from Reddit!")
    async def meme(self, ctx):
         rmeme = handler.get("https://meme-api.com/gimme")
         jmeme = json.loads(rmeme.text)
         
         embed = discord.Embed(
              title = jmeme["title"],
              description = "Upvote score: {0}".format(jmeme["ups"]),
              color = discord.Colour.blurple(),
         )
         embed.set_image(url=jmeme["url"])
         embed.set_footer(text="Posted in r/{0} by u/{1}".format(jmeme["subreddit"], jmeme["author"]))

         await ctx.respond(embed=embed)

    @group.command(name="randombreed", description="Get a random dog breed!")
    async def randombreeed(self, ctx):
               rbreed = handler.get("https://dog.ceo/api/breeds/list/all")
               breeds = list(json.loads(rbreed.text)["message"].keys())
               randbreed = random.choice(breeds)
               
               await ctx.respond(f":dog: `{randbreed}`")

    @group.command(name="urlshort", description="Shortens a given URL")
    async def urlshort(self, ctx, url: discord.Option(str, description="URL to shorten. Must begin with http(s)://www.")):
           ctx.defer()
           rurl = requests.post("https://csclub.uwaterloo.ca/~phthakka/1pt-express/addURL", params={"long": url})
           jurl = json.loads(rurl.text)
           await ctx.respond("Your Shortened URL: https://1pt.co/{0}".format(jurl["short"]))

    @group.command(name="weather", description="Get the weather for a city!")
    async def weather(self, ctx, city: discord.Option(str, description="The city to get weather of")):
        request = requests.get("https://goweather.herokuapp.com/weather/{0}".format(city))
        response = json.loads(request.text)
        if request.status_code == 404:
                  await ctx.respond(":x: City not found! Maybe you misspelt it?")
                  return
        embed = discord.Embed(
               title = "Weather in {0}".format(city.upper()),
        )
        embed.add_field(name="Today", value="Temperature is {0}, wind is up to {1} and it's {2}.".format(response["temperature"], response["wind"], response["description"]))
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)

        for day in response["forecast"]:
               embed.add_field(name="Day {}".format(day["day"]), value="Temperture is {0} and wind is up to {1}.".format(day["temperature"], day["wind"]))

        await ctx.respond(embed=embed)
           

    @group.command(name="httpdog", description="Get a dog image for an HTTP status code!")
    async def httpdog(self, ctx, status: discord.Option(str, description="The HTTP status code to get image of.")):
           rurl = requests.get("https://http.dog/{0}.jpg".format(status))
           if rurl.status_code == 404:
                  await ctx.respond(":x: Dog not found! That status code does not exist.")
                  return
    
           embed = discord.Embed(
                  title="Dog {0}".format(status),
                  color=discord.Colour.blurple(),
           )
           embed.set_image(url="https://http.dog/{0}.jpg".format(status))
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           await ctx.respond(embed=embed)

    @group.command(name="pokedex", description="Get info on a pokemon!")
    async def pokedex(self, ctx, pokemon: discord.Option(str, description="Pokemon to get data of")):
           request = requests.get("https://pokeapi.co/api/v2/pokemon/{0}".format(pokemon.lower()))
           
           if request.status_code == 404:
                  await ctx.respond(":x: Pokemon not found! Maybe you misspelled it?")
                  return
           
           response = json.loads(request.text)

           abilities = ""

           for ability in response["abilities"]:
                  abilities = abilities + "{}, ".format(ability["ability"]["name"])

           embed = discord.Embed(
                  title="Info on {0}".format(pokemon),
                  description="""
                  **Abilities:** {0}
**Base XP:** {1}
**Order:** {2}
**Weight:** {3}
**Height:** {4}




                 """.format(abilities, response["base_experience"], response["order"], response["weight"], response["height"]),
           )
           embed.set_thumbnail(url=response["sprites"]["front_default"])
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           await ctx.respond(embed=embed)

    @group.command(name="dictionary", description="Get the definition of an english word!")
    async def dictionary(self, ctx, word: discord.Option(str, description="Word to get definition of")):
           request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
           if request.status_code == 404:
                  await ctx.respond(":x: Word \"**{}**\" not found! Perhaps you misspelled it?".format(word))
                  return
           response = json.loads(request.text)
           response = response[0]
           description = ""
           for definitions in response["meanings"]:
                  description = description + "_{0} usage:_ {1}\n".format(
                         definitions["partOfSpeech"],
                         definitions["definitions"][0]["definition"]
                  )

           embed = discord.Embed(
                  title = "Definition of {0}".format(word),
                  description=description,
                  color=discord.Colour.blurple(),
           )
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           await ctx.respond(embed=embed)

    @group.command(name="fakeperson", description="Generates a fake person and their info")
    async def fakeperson(self, ctx):
           request = requests.get("https://randomuser.me/api/")
           response = json.loads(request.text)
           response = response["results"][0]
           embed = discord.Embed(
                  title="{0}. {1} {2}, {3}".format(response["name"]["title"], response["name"]["first"], response["name"]["last"], response["gender"])
           )
           embed.set_image(url=response["picture"]["large"])
           embed.add_field(name="Street", value="{0} {1}".format(response["location"]["street"]["number"], response["location"]["street"]["name"]))
           embed.add_field(name="Location", value="{0}, {1}, {2}".format(response["location"]["city"], response["location"]["state"], response["location"]["country"]))
           embed.add_field(name="Email", value=response["email"])
           embed.add_field(name="Age", value="Born on {0}, age {1}".format(response["dob"]["date"], response["dob"]["age"]))
           embed.add_field(name="Phone Number", value=response["phone"])
           await ctx.respond(embed=embed)
    
    @group.command(name="bible", description="Get a verse from the Bible!")
    async def bible(self, ctx, book: discord.Option(str, description="Name of book to get verse from."), chapter: discord.Option(str, description="Chapter to get verse from"), verse: discord.Option(str, description="Verse to get text from")):
           request = requests.get("https://bible-api.com/{0}%20{1}:{2}".format(book, chapter, verse))
           if request.status_code == 404:
                  await ctx.respond(":x: Book/Chapter/Verse not found!")
                  return
           response = json.loads(request.text)
           response = response["verses"][0]
           embed = discord.Embed(
                  title="{0} {1}:{2}".format(response["book_name"], response["chapter"], response["verse"]),
                  description="_{}_".format(response["text"]),
                  color=discord.Colour.blurple(),
           )
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           await ctx.respond(embed=embed)
           
                  

           

    

           

   
           
        
    
         
         
         
        

        








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Apis(bot)) # add the cog to the bot

