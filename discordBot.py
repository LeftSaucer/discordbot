import os
import discord
from discord.ext import commands
from python_aternos import Client

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

# Set up the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def startserver(ctx):
    if ctx.channel.name == 'start-server':
        try:
            atclient = Client()
            atclient.login(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
            aternos = atclient.account
            servs = aternos.list_servers()
            myserv = servs[0]
            myserv.start()
            response = 'Server starting...'
        except Exception as e:
            response = f"Failed to start the server: {str(e)}"
        await ctx.send(response)
    else:
        await ctx.send("This command can only be used in the 'start-server' channel.")

# Load the bot token securely from environment variables
bot_token = os.getenv('DISCORD_BOT_TOKEN')
if bot_token:
    bot.run(bot_token)
else:
    print("Bot token is not set. Please set the DISCORD_BOT_TOKEN environment variable.")
