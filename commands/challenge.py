import discord
import openai
import asyncio
from discord import app_commands
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY



# This command will let the user to challenge a user for roast battle
# This will have a 60 second time for the user to give the input


