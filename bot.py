import os
import discord
from discord.ext import commands
from flask import Flask
import threading

# 簡易Webサーバー
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

threading.Thread(target=run_web).start()

# Discord Bot
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

