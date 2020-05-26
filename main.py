

import discord
import random
from pyngrok import ngrok,exception
import os
from time import sleep

ngrok.set_auth_token("")

prefix = "--"

prikazy = ["help" , "ngrok"]

client = discord.Client()

@client.event
async def on_ready():
    print("bot is online!")
    try:
        ngrok.connect(22,proto="tcp",region="eu")
    except Exception:
        print("Exception occured, reloading")
        sleep(15)
        on_ready()

@client.event
async def on_message(message):
    channel = message.channel
    if str(channel) == "ssh":
        if message.content == f"{prefix}{prikazy[0]}":              # --help
            string = "Dostupné příkazy:\n"
            for prikaz in prikazy:
                string += f"  {prefix}{prikaz}\n"
            await channel.send(string)
        elif message.content == f"{prefix}{prikazy[1]}":            # --ngrok
            tunels = ngrok.get_tunnels()
            string = "Aktivní tunely:\n"
            for tunel in tunels:
                string += f"  {tunel}\n"
            await channel.send(string)


client.run("")
