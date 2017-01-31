#!/usr/bin/python3

import discord
import asyncio
import httplib2
import os
import ConfigParser


# Get keys from config file
config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))
TOKEN = config.get('Keys', 'token')

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith('.test'):
        await client.send_message(message.channel, 'Here is a test message')

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
