from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.depends import get_db
from app.crud.channel import channel_crud
from app.schemas.channel import ChannelRead, ChannelCreate, ChannelUpdate

router = APIRouter(prefix="/channels", tags=["Channels"])



@router.post("/", response_model=ChannelRead)
async def create_channel(data: ChannelCreate, db: AsyncSession = Depends(get_db)):
    return await channel_crud.create(db, data)


@router.get("/", response_model=list[ChannelRead])
async def get_channels(db: AsyncSession = Depends(get_db)):
    return await channel_crud.get_all(db)


@router.get("/{channel_id}", response_model=ChannelRead)
async def get_channel(channel_id: int, db: AsyncSession = Depends(get_db)):
    return await channel_crud.get(db, channel_id)


@router.put("/{channel_id}", response_model=ChannelRead)
async def update_channel(channel_id: int, data: ChannelUpdate, db: AsyncSession = Depends(get_db)):
    return await channel_crud.update(db, channel_id, data)


@router.delete("/{channel_id}")
async def delete_channel(channel_id: int, db: AsyncSession = Depends(get_db)):
    return await channel_crud.delete(db, channel_id)
