import uuid
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import BigInteger, Boolean, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    device_id: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    promocode: Mapped[str] = mapped_column(String(50))
    referal_promocode: Mapped[str] = mapped_column(String(50))
    is_fake: Mapped[bool] = mapped_column(Boolean, default=False)
    is_subscription: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())