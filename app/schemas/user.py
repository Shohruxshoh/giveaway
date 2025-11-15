from pydantic import BaseModel

class UserBase(BaseModel):
    telegram_id: int
    device_id: str
    username: str
    promocode: str
    referal_promocode: str
    is_fake: bool
    is_subscription: bool

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: str
