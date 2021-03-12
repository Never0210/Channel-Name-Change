import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio

TOKEN = 'DEIN-BOT-TOKEN' # Füge hier dein Bot-Token ein 

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Loggt sich ein als: {bot.user.name}')
    print(f'Mit der ID: {bot.user.id}')
    await bot.loop.create_task(status_task())

async def status_task():
    channel = bot.get_channel(DEINE-CHANNEl-ID) # ID des Channels
    while True:
        await channel.edit(name="DEIN-CHANNEL-NAME1") # Füge hier den ersten Channel Namen ein zu dem gewechselt werden soll.
        await asyncio.sleep(310) # Hier die sleep dauer // Nicht unter 300 [Discord - RateLimit]
        await channel.edit(name="DEIN-CHANNEL-NAME2") # Füge hier den zweiten Channel Namen ein zu dem gewechselt werden soll.
        await asyncio.sleep(310) # Hier die sleep dauer // Nicht unter 300 [Discord - RateLimit]

bot.run(TOKEN)


# Made by Never0210
# Bei Fragen oder Hilfe an mich!