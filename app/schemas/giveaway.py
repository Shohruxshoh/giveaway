from typing import Optional
from pydantic import BaseModel

# =========================
# GIVEAWAY INFO SCHEMAS
# =========================
class GiveawayInfoBase(BaseModel):
    giveaway_about_title_uz: str
    giveaway_about_description_uz: str
    giveaway_about_title_ru: str
    giveaway_about_description_ru: str
    giveaway_about_title_en: str
    giveaway_about_description_en: str
    auto_join_title_uz: str
    auto_join_description_uz: str
    auto_join_title_ru: str
    auto_join_description_ru: str
    auto_join_title_en: str
    auto_join_description_en: str


class GiveawayInfoCreate(GiveawayInfoBase):
    pass


class GiveawayInfoUpdate(BaseModel):
    giveaway_about_title_uz: Optional[str] = None
    giveaway_about_description_uz: Optional[str] = None
    giveaway_about_title_ru: Optional[str] = None
    giveaway_about_description_ru: Optional[str] = None
    giveaway_about_title_en: Optional[str] = None
    giveaway_about_description_en: Optional[str] = None
    auto_join_title_uz: Optional[str] = None
    auto_join_description_uz: Optional[str] = None
    auto_join_title_ru: Optional[str] = None
    auto_join_description_ru: Optional[str] = None
    auto_join_title_en: Optional[str] = None
    auto_join_description_en: Optional[str] = None


class GiveawayInfoRead(GiveawayInfoBase):
    id: int
