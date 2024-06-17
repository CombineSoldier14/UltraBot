import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime
import uuid
import random
import string
import cogs.lists
from cogs.lists import aaquotes
from cogs.lists import suntzuquotes
from cogs.lists import ytvalues
import requests
import time
import json
import uuid
import string
import random
import time
import cogs.requestHandler as handler


with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]


with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

with open("latestaddition.json", "r") as f:
            _r = json.load(f)
            LATESTADDITION = _r["LATEST_ADDITION"]



#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"
            prefix = "-"


if dev_status == "false":
            name = "CombineBot"
            game = "combinesoldier14.site"
            icon = "https://i.postimg.cc/j5YGqs0n/f66bd4beb4f1ebee0685d8c5cfd646bb.png"
            prefix = ";"


def makeEmbed(**kwargs):
        embed = discord.Embed(**kwargs)
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon) 
        return embed


def getRandomString(length):
        if length > 100:
              return ":x: Specified length is too high!"
              
         
        chars = []

        for c in string.ascii_lowercase:
              chars.append(c)

        for c in string.ascii_uppercase:
              chars.append(c)

        for c in range(10): # 1-9
              chars.append(str(c))
              
        randstring = ""

        for s in range(length):
              randstring = randstring + random.choice(chars)

        return "`{}`".format(str(randstring))


def getSunTzu():
        quotes = suntzuquotes
        return random.choice(quotes)


def getAceAttorneyQuote():
        quotes = aaquotes
        return random.choice(quotes)

def getYTvideo():
        videoid = ""
        for _ in range(11): # video id is 11 chars long
            videoid = videoid + random.choice(ytvalues)
         
        return "https://www.youtube.com/watch?v={}".format(videoid)

def getDNDmod(mod):
        d = requests.get("https://www.dnd5eapi.co/api/ability-scores/{}".format(mod.lower()))
        j = json.loads(d.text)
        return j

def getJoke():
        r = handler.get("https://official-joke-api.appspot.com/random_joke")
        j = json.loads(r.text)
        return "{0} {1}".format(j["setup"], j["punchline"])

def getXKCD(recent, number):
        if recent == False:
                xkcdlink = handler.get("https://xkcd.com/" + str(number) + "/info.0.json")
                xkcdjson = json.loads(xkcdlink.text)
                return xkcdjson
        elif recent == True:
                xkcdlink = handler.get("https://xkcd.com/info.0.json")
                xkcdjson = json.loads(xkcdlink.text)
                return xkcdjson
        
def getDogPic():
        doglink = handler.get("https://dog.ceo/api/breeds/image/random")
        dogjson = json.loads(doglink.text)
        return dogjson

def getShakespeare(text):
        rshake = handler.get("https://api.funtranslations.com/translate/shakespeare.json?text={0}".format(text))
        jshake = json.loads(rshake.text)
        return jshake

def getStand():
        id = random.randint(1, 155)
        rstand = handler.get("https://stand-by-me.herokuapp.com/api/v1/stands/{0}".format(str(id)))
        jstand = json.loads(rstand.text)
        return jstand
def getJoe():
        id = random.randint(1, 155)
        rchar = handler.get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(str(id)))
        jchar = json.loads(rchar.text)
        return jchar

def getMeme():
        rmeme = handler.get("https://meme-api.com/gimme")
        jmeme = json.loads(rmeme.text)
        return jmeme

def getRandBreed():
        rbreed = handler.get("https://dog.ceo/api/breeds/list/all")
        breeds = list(json.loads(rbreed.text)["message"].keys())
        randbreed = random.choice(breeds)
        return randbreed

def shortenURL(url):
        rurl = requests.post("https://csclub.uwaterloo.ca/~phthakka/1pt-express/addURL", params={"long": url})
        jurl = json.loads(rurl.text)
        return jurl["short"]

def getWeather(city):
        request = requests.get("https://goweather.herokuapp.com/weather/{0}".format(city))
        response = json.loads(request.text)
        if request.status_code == 404:
          return ":x: City not found! Maybe you misspelt it?"
        else:
          return response

def getPoke(pokemon, ctx=discord.context.ApplicationContext):
        request = requests.get("https://pokeapi.co/api/v2/pokemon/{0}".format(pokemon.lower()))
           
        if request.status_code == 404:
                  return ":x: Pokemon not found! Maybe you misspelled it?"
                  
                  
           
        response = json.loads(request.text)
        return response 

def getPerson():
         request = requests.get("https://randomuser.me/api/")
         response = json.loads(request.text)
         return response    

def getBible(book, chapter, verse):
        request = requests.get("https://bible-api.com/{0}%20{1}:{2}".format(book, chapter, verse))
        if request.status_code == 404:
                  return ":x: Book/Chapter/Verse not found!"
        response = json.loads(request.text)
        return response

async def getUserInfo(bot, user, ctx=discord.context.ApplicationContext):
        if bot == True:
                info = {
                        "id":user.id,
                        "joineddiscord":user.created_at,
                        "discriminator":user.discriminator,
                        "avatar":user.avatar,
                        "bot":"No"
                }
                 
        if bot == False:
                info = {
                        "id":user.id,
                        "joineddiscord":user.created_at,
                        "avatar":user.avatar,
                        "bot":"No"
                }
        return info

async def getChannelInfo(channel, ctx=discord.context.ApplicationContext):
        info = {
                "category":channel.category,
                "createdat":channel.created_at,
                "guild":channel.guild,
                "id":channel.id,
                "nsfw":channel.nsfw,
                "slowmode":channel.slowmode_delay,
                "type":channel.type
        }
        return info

async def getServerInfo(server, ctx=discord.context.ApplicationContext):
        info = {
                "members":server.member_count,
                "owner":server.owner,
                "id": server.id,
                "createdat":server.created_at,
                "description":server.description,
                "icon":server.icon

        }
        return info

        


















































        
        

















































