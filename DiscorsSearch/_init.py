import os 
import discord as searchBot
import requests
import sys
__discordAPIKey = "" # Discord Bot API Secret Key
__client = searchBot.Client()

async def __convertUUID(_argument):
    os.system('cls || clear')
    try:
        discordUser = await __client.fetch_user(_argument)
        _data = {
            "Discord UUID": discordUser.id, # Discord UUID 
            "Discord Tag": discordUser.name + "#" + discordUser.discriminator, # Discord Full Name and Tag
            "Discord Creation": discordUser.created_at, # Discord Creation Date
            "Discord Avatar URL": discordUser.avatar_url, # Discord Avatar URL
            "Discord Bot": discordUser.bot, # Discord Bot Status
        }
        print("Discord UUID         :: " + str(_data['Discord UUID']))
        print("Discord Tag          :: " + str(_data['Discord Tag']))
        print("Discord Creation     :: " + str(_data['Discord Creation']))
        print("Discord Avatar URL   :: " + str(_data['Discord Avatar URL']))
        print("Discord Bot          :: " + str(_data['Discord Bot']))
        await on_ready()
    except:
        print("Failed To Fetch ID")
        await on_ready()
@__client.event
async def on_ready():
    print('\n')
    regInput = input("Enter Discord UUID: ")
    runtime = await __convertUUID(regInput)
__client.run(__discordAPIKey)








