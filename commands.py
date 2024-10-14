import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

game_stats = {
    'player1': {'game1': 150, 'game2': 200},
    'player2': {'game1': 180, 'game2': 220}
}

# Use a tuple for immutable data
supported_games = ('game1', 'game2')

@lru_cache(maxsize=128)  # Decorate to use LRU cache
async def fetch_stats_from_api(game, players):
    """
    Placeholder function for fetching game stats from an external API.
    Assume this function batches requests to fetch stats for multiple players in a single API call.
    Modify to use actual API calls in your implementation.
    The decorator lru_cache is used here for demonstration; in practice,
    async functions require an async-compatible cache decorator.
    """
    api_response = {
        'player1': {'game1': 150, 'game2': 200},
        'player2': {'game1': 180, 'game2': 220}
    }
    return {player: api_response.get(player, {}).get(game) for player in players}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='stats', help='Retrieves stats for the specified game. Usage: !stats <game_name> <player_name>')
async def fetch_stats(ctx, game: str, player: str):
    if game in supported_games:
        player_stats = (await fetch_stats_from_api(game, tuple([player]))).get(player) # Async function call adjustment required for actual usage
        if player_stats:
            await ctx.send(f"{player}'s stats for {game}: {player_stats}")
        else:
            await ctx.send("Stats not found. Make sure the player name and game are correct.")
    else:
        await ctx.send(f"{game} is not supported. Use !games to list supported games.")

bot.run(TOKEN)