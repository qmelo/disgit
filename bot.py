import asyncio

from discord.ext import commands
from fastapi import FastAPI

from routers import hello
from settings import DISCORD_BOT_TOKEN

app = FastAPI()
app.include_router(hello.router, prefix='/hello')

bot = commands.Bot('$')
bot.load_extension('cogs.ping')

asyncio.create_task(bot.start(DISCORD_BOT_TOKEN))
