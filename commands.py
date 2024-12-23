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

supported_games = ('game1', 'game2')

async def fetch_stats_from_api(game, players):
    api_response = {
        'player1': {'game1': 150, 'game2': 200},
        'player2': {'game1': 180, 'game2': 220}
    }
    if game not in supported_games:
        raise ValueError("Unsupported game requested")
    return {player: api_response.get(player, {}).get(game) for player in players}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='stats', help='Retrieves stats for the specified game. Usage: !stats <game_name> <player_name>')
async def fetch_stats(ctx, game: str, player: str):
    try:
        if game in supported_games:
            player_stats = (await fetch_stats_from_api(game, tuple([player]))).get(player)
            if player_stats is not None:
                await ctx.send(f"{player}'s stats for {game}: {player_stats}")
            else:
                await ctx.send("Stats not found. Make sure the player name and game are correct.")
        else:
            await ctx.send(f"{game} is not supported. Use !games to list supported games.")
    except Exception as e:
        await ctx.send(f"Error occurred: {str(e)}")

@bot.command(name='games', help='Lists all supported games.')
async def list_games(ctx):
    games_list = ', '.join(supported_games)
    await ctx.send(f"Supported games are: {games_list}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't understand that command. Type !help for a list of commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing a required argument. Please check the command format and try again.")
    else:
        await ctx.send("An unexpected error occurred. Please try again later.")

bot.run(TOKEN)