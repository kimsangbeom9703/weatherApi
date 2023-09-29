from typing import Optional

from pydantic import BaseModel

# Shared properties
class AreaBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class AreaCreate(AreaBase):
    title: str


# Properties to receive on item update
class AreaUpdate(AreaBase):
    pass


# Properties shared by models stored in DB
class AreaInDBBase(AreaBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Item(AreaInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(AreaInDBBase):
    pass