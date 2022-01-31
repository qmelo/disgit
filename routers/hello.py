from fastapi import APIRouter
from bot import bot

router = APIRouter()

@router.get('/world')
async def hello_world():
    TEST_CHANNEL_ID = 917782507041206306
    channel = bot.get_channel(TEST_CHANNEL_ID)
    await channel.send('hello, world')
    return {'hello', 'world'}
