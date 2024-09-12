import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

game_stats = {
    'player1': {'game1': 150, 'game2': 200},
    'player2': {'game1': 180, 'game2': 220}
}

supported_games = ['game1', 'game2']

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='stats', help='Retrieves stats for the specified game. Usage: !stats <game_name> <player_name>')
async def fetch_stats(ctx, game: str, player: str):
    if game in supported_games:
        player_stats = game_stats.get(player, {}).get(game)
        if player_stats:
            await ctx.send(f"{player}'s stats for {game}: {player_stats}")
        else:
            await ctx.send("Stats not found. Make sure the player name and game are correct.")
    else:
        await ctx.send(f"{game} is not supported. Use !games to list supported games.")

@bot.command(name='compare', help='Compares stats between two players. Usage: !compare <game_name> <player1> <player2>')
async def compare_stats(ctx, game: str, player1: str, player2: str):
    if game in supported_games:
        stats1 = game_stats.get(player1, {}).get(game)
        stats2 = game_stats.get(player2, {}).get(game)
        if stats1 and stats2:
            comparison = "equal to" if stats1 == stats2 else "higher than" if stats1 > stats2 else "lower than"
            await ctx.send(f"{player1}'s stats for {game} ({stats1}) are {comparison} {player2}'s ({stats2}).")
        else:
            await ctx.send("One or both players' stats not found.")
    else:
        await ctx.send(f"{game} is not supported. Use !games to list supported games.")

@bot.command(name='games', help='Lists all supported games.')
async def list_games(ctx):
    games_list = ', '.join(supported_games)
    await ctx.send(f"Supported games: {games_list}")

bot.run(TOKEN)