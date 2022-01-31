from fastapi import APIRouter

router = APIRouter()

@router.get('/world')
async def hello_world():
    return {'hello', 'world'}
    