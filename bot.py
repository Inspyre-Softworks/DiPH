#!/usr/bin/env python

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class DiphBot(discord.Client):

    async def on_ready(self):
        print(f'{self.client.user.name} has connected to Discord!')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
        print(dir(member))
    
    async def on_typing(self):
        print('Someone is typing')
        
    def __init__(self):
        self.run()
        
        
if __name__ == '__main__':
    DiphBot()
        
