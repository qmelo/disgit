from fastapi import APIRouter
from bot import bot

router = APIRouter()

@router.get('/hello/world')
async def hello_world():
    TEST_CHANNEL_ID = 917782507041206306
    channel = bot.get_channel(TEST_CHANNEL_ID)
    await channel.send('hello, world')
    return {'hello', 'world'}

@router.get('/channels')
async def channels(guild_id: int):
    guild = bot.get_guild(guild_id)
    items = []
    for channel in guild.channels:
        item = {}
        item['name'] = channel.name
        item['id'] = channel.id
        item['type'] = channel.type.name
        items.append(item)
    return {'channels': items}
