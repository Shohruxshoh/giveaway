from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.channel import Channel
from app.schemas.channel import ChannelCreate, ChannelUpdate


class ChannelCRUD:

    async def create(self, db: AsyncSession, data: ChannelCreate) -> Channel:
        new_channel = Channel(**data.model_dump())
        db.add(new_channel)
        await db.commit()
        await db.refresh(new_channel)
        return new_channel

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Channel))
        return result.scalars().all()

    async def get(self, db: AsyncSession, channel_id: int):
        result = await db.execute(
            select(Channel).where(Channel.id == channel_id)
        )
        return result.scalars().first()

    async def update(self, db: AsyncSession, channel_id: int, data: ChannelUpdate):
        channel = await self.get(db, channel_id)
        if not channel:
            return None

        for field, value in data.model_dump(exclude_none=True).items():
            setattr(channel, field, value)

        db.add(channel)
        await db.commit()
        await db.refresh(channel)
        return channel

    async def delete(self, db: AsyncSession, channel_id: int):
        channel = await self.get(db, channel_id)
        if not channel:
            return None

        await db.delete(channel)
        await db.commit()
        return True


channel_crud = ChannelCRUD()
