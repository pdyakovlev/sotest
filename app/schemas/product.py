from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
