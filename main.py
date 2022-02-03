import asyncio

from fastapi import FastAPI

from bot import bot
from routers import hello
from settings import DISCORD_BOT_TOKEN

app = FastAPI()
app.include_router(hello.router, prefix='')

bot.load_extension('cogs.ping')

asyncio.create_task(bot.start(DISCORD_BOT_TOKEN))
