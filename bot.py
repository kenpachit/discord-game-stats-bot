import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        try:
            await message.channel.send('Hello!')
        except discord.DiscordException as e:
            print(f'Error responding to hello: {e}')

@client.event
async def on_error(event, *args, **kwargs):
    with open('discord_bot_error.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

try:
    client.run(TOKEN)
except discord.LoginFailure:
    print("Invalid token; please check your DISCORD_TOKEN environment variable.")
except discord.DiscordException as general_exception:
    print(f"An error occurred: {general_exception}")