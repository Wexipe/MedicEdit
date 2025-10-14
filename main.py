import discord
import asyncio
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = 1427675582870847663

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("❌ کانال پیدا نشد — بررسی کن بات در سرور هست و CHANNEL_ID درسته.")
        return
    while True:
        await channel.send("سلام 😄")
        await asyncio.sleep(5)

client.run(TOKEN)
