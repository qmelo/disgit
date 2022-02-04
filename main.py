import asyncio

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from bot import bot
from routers import hello
from settings import DISCORD_BOT_TOKEN

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(hello.router, prefix='/api')

bot.load_extension('cogs.ping')

asyncio.create_task(bot.start(DISCORD_BOT_TOKEN))
