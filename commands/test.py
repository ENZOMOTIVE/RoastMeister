import discord
from discord import app_commands

@app_commands.command(name="test", description="Test if the bot is running")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Bot is working", ephemeral=True)
