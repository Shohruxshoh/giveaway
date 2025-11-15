from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.depends import get_db
from app.crud.giveaway import giveaway_crud
from app.schemas.giveaway import GiveawayInfoRead, GiveawayInfoCreate, GiveawayInfoUpdate

router = APIRouter(prefix="/giveaway", tags=["GiveawayInfo"])


@router.post("/", response_model=GiveawayInfoRead)
async def create_giveaway(data: GiveawayInfoCreate, db: AsyncSession = Depends(get_db)):
    return await giveaway_crud.create(db, data)


@router.get("/", response_model=list[GiveawayInfoRead])
async def get_giveaways(db: AsyncSession = Depends(get_db)):
    return await giveaway_crud.get_all(db)


@router.get("/{item_id}", response_model=GiveawayInfoRead)
async def get_giveaway(item_id: int, db: AsyncSession = Depends(get_db)):
    return await giveaway_crud.get(db, item_id)


@router.put("/{item_id}", response_model=GiveawayInfoRead)
async def update_giveaway(item_id: int, data: GiveawayInfoUpdate, db: AsyncSession = Depends(get_db)):
    return await giveaway_crud.update(db, item_id, data)


@router.delete("/{item_id}")
async def delete_giveaway(item_id: int, db: AsyncSession = Depends(get_db)):
    return await giveaway_crud.delete(db, item_id)
