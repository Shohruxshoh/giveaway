class Channel:
    id: int
    channel_id: int # BigIntager
    username: str

class GiveawayInfo:
    id: int
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

class User:
    id: str # UUID
    telegram_id: int # BigIntager
    device_id: str
    username: str
    promocode: str
    referal_promocode: str
    is_fake: bool
    is_subscription: bool

class Ticket:
    id: int
    user_id: str # UUID

