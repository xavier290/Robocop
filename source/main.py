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
            "$python for the python channel",
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
    if message.content.startswith("$help.code"):
        await message.channel.send("https://stackoverflow.com/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    if message.content.startswith("$help"):
        await message.channel.send(help)












@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    py_channel_id = 800707938405974016
    if message.channel.id == py_channel_id:
        if message.content.startswith("$python"):
            await message.channel.send("https://devdocs.io/python~3.9/")




@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    go_channel_id = 800707959041556551
    if message.channel.id == go_channel_id:
        if message.content.startswith("$golang"):
            await message.channel.send("https://devdocs.io/go/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    ja_channel_id = 800707914536583208
    if message.channel.id == ja_channel_id:
        if message.content.startswith("$java"):
            await message.channel.send("https://docs.oracle.com/en/java/")

@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    php_channel_id = 800707986292736031
    if message.channel.id == php_channel_id:
        if message.content.startswith("$php"):
            await message.channel.send("https://devdocs.io/phpunit~9/")

@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    c_lang_channel_id = 800708001098367037
    if message.channel.id == c_lang_channel_id:
        if message.content.startswith("$python"):
            await message.channel.send("https://devdocs.io/c/ https://devdocs.io/cpp/")

@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    web_channel_id = 800708015409594389
    if message.channel.id == web_channel_id:
        if message.content.startswith("$web"):
            await message.channel.send("https://devdocs.io/html/element/heading_elements https://devdocs.io/css/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    rus_channel_id = 800708036724260914
    if message.channel.id == rus_channel_id:
        if message.content.startswith("$rust"):
            await message.channel.send("https://devdocs.io/rust/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    rb_channel_id = 800708046455701504
    if message.channel.id == rb_channel_id:
        if message.content.startswith("$ruby"):
            await message.channel.send("https://devdocs.io/ruby~3/")


@client.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    lu_channel_id = 800708060573859860
    if message.channel.id == lu_channel_id:
        if message.content.startswith("$lu"):
            await message.channel.send("https://devdocs.io/lua~5.4/")

client.run("ODAxNTY3MTg2NDcyMDA5NzQ5.YAijnQ.tutnC3BEyE6sQKRkwY0H6BSMIyI")






