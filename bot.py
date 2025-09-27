import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "おはよう":
        await message.channel.send("おやすみ")
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
