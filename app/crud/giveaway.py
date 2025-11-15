from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.giveaway import GiveawayInfo
from app.schemas.giveaway import GiveawayInfoCreate, GiveawayInfoUpdate


class GiveawayCRUD:

    async def create(self, db: AsyncSession, data: GiveawayInfoCreate):
        item = GiveawayInfo(**data.model_dump())
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(GiveawayInfo))
        return result.scalars().all()

    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(
            select(GiveawayInfo).where(GiveawayInfo.id == id)
        )
        return result.scalars().first()

    async def update(self, db: AsyncSession, id: int, data: GiveawayInfoUpdate):
        item = await self.get(db, id)
        if not item:
            return None

        for field, value in data.model_dump(exclude_none=True).items():
            setattr(item, field, value)

        await db.commit()
        await db.refresh(item)
        return item

    async def delete(self, db: AsyncSession, id: int):
        item = await self.get(db, id)
        if not item:
            return None

        await db.delete(item)
        await db.commit()
        return True


giveaway_crud = GiveawayCRUD()
