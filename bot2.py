#!/usr/bin/env python

import os
import discord
from inspyred_print import Color, Format
from dotenv import load_dotenv
from


fmt_end = Format.end_mod
red = Color.red

load_dotenv()
client = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")

# print(dir(client))


@client.event
async def on_ready():
    """Short summary.

    Returns
    -------
    def
        Description of returned object.

    Raises
    -------
    ExceptionName
        Why the exception is raised.

    Examples
    -------
    Examples should be written in doctest format, and
    should illustrate how to use the function/class.
    >>>

    """
    print(f"{red}We have logged in as {client.user}{fmt_end}")
    # print(dir(client))
    print(client.users)


cmd_prefix = "$"
attr_prefix = "."


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    sender = message.author
    content = message.content

    # First, let's check to see if our received message is a request to change an attribute
    if content.startswith(attr_prefix):
        content == content.split(" ").pop()

    if content.startswith("$hello"):
        await message.channel.send("Hello!")
        await message.channel.send(f"{dir(message)}")
        await message.tts(message)

    elif content.startswith(f"{cmd_prefix}weather"):
        print(f"Received request from {sender} to fetch weather")
        await message.channel.send("Here I would deliver the weather.")
        print("Responded")

    else:
        msg_statement = f"{sender} sent a message to {message.channel}:\n{content}"
        if not content == "":
            print(msg_statement)
    print("")


@client.event
async def on_member_join(member):
    print(f"{member.name} joined at {member.joined_at}")
    print(dir(member))


client.run(TOKEN)

for each in client.users:
    print(client.fetch_user(each["id"]))

print(client.user)
thing = client.user
print(dir(thing))
print(dir(client.user))
