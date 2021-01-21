import discord
import asyncio
from discord.ext import commands

client = discord.Client()
help = [
    {
        "commands for text channels": {
            "$help",
        },
        "commands for learning channels": {
            "$python for the python channel"
            "$help.code for helping with code errors"

        }
    }
]




@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello! ")




@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    channel_id = 800707938405974016
    if message.channel.id == channel_id:
        if message.content.startswith("$python"):
            await message.channel.send("https://devdocs.io/python~3.9/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    if message.content.startswith("$help.code"):
        await message.channel.send("https://stackoverflow.com/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    if message.content.startswith("$help"):
        await message.channel.send(help)


client.run("Token here")






