import discord
import openai
import os
from discord import app_commands
from commands import test
from config import TOKEN, OPENAI_API_KEY




#define intents for Bot Setup
intents= discord.Intents.default()
intents.messages = True
intents.reactions = True

# Create instance of bot
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

#tells discord.py that the following event will be triggered when the thing started
@bot.event
async def on_ready():
    await tree.sync() # Sync slash commands
    print(f"{bot.user} is online and running")


#Load Commands
tree.add_command(test.test)

# Starts the bot using the Auth token
bot.run(TOKEN)
