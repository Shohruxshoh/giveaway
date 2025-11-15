from pydantic import BaseModel

class TicketBase(BaseModel):
    user_id: str

class TicketCreate(TicketBase):
    pass

class TicketOut(TicketBase):
    id: int
