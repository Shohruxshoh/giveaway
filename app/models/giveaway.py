from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class GiveawayInfo(Base):
    __tablename__ = "giveaway_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    giveaway_about_title_uz: Mapped[str] = mapped_column(String(255))
    giveaway_about_description_uz: Mapped[str] = mapped_column(String(500))
    giveaway_about_title_ru: Mapped[str] = mapped_column(String(255))
    giveaway_about_description_ru: Mapped[str] = mapped_column(String(500))
    giveaway_about_title_en: Mapped[str] = mapped_column(String(255))
    giveaway_about_description_en: Mapped[str] = mapped_column(String(500))

    auto_join_title_uz: Mapped[str] = mapped_column(String(255))
    auto_join_description_uz: Mapped[str] = mapped_column(String(500))
    auto_join_title_ru: Mapped[str] = mapped_column(String(255))
    auto_join_description_ru: Mapped[str] = mapped_column(String(500))
    auto_join_title_en: Mapped[str] = mapped_column(String(255))
    auto_join_description_en: Mapped[str] = mapped_column(String(500))

