from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True
