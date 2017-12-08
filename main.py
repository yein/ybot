#import logging
#import requests
#import discord
#import asyncio
#import lxml

# Set up local data structures from /data

straight_fapcams = []
not_straight_fapcams = []
top_1k_albums = []


def load_data():
  straight_fapcams = [line.rstrip('\n') for line in open('straight-fapcams')]

load_data()

for x in straight_fapcams:
  print(x + "\n")

if not straight_fapcams:
  print "Nothing here!"

'''
# Configure discordpy login module
logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('token')
'''
