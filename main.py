import os

import discord
import dotenv
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('.env')


client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ez(ctx):
  channel= client.get_channel(829690126371913761)
  await channel.send('hello')

@client.event
async def on_ready():
    print("connected")




client.run(os.getenv('DISCORD_TOKEN'))








