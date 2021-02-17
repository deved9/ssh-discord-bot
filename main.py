import discord
from pyngrok import ngrok,exception
import os
from time import sleep

#paste ngrok authtoken here
ngrok.set_auth_token("")

#prefix for bots commands
prefix = "--"

#list of available commands to print when asked for help
commands = ["help" , "ngrok"]

client = discord.Client()

@client.event
async def on_ready():
    print("bot is online!")
    try:
        #here you can add your custom ngrok tunnels
        ngrok.connect(22,proto="tcp",region="eu")
    except Exception as e:
        print(f"Exception occured, reloading\n{e}")
        sleep(15)
        on_ready()

@client.event
async def on_message(message):
    channel = message.channel
    
    #only works in channel with name "ssh"
    if str(channel) == "ssh":
        if message.content == f"{prefix}{commands[0]}":              # --help
            string = "Available commands:\n"
            for command in commands:
                string += f"  {prefix}{command}\n"
            await channel.send(string)
        elif message.content == f"{prefix}{commands[1]}":            # --ngrok
            tunels = ngrok.get_tunnels()
            string = "Active tunnels:\n"
            for tunel in tunels:
                string += f"  {tunel}\n"
            await channel.send(string)

#paste discord bot token here
client.run("")
