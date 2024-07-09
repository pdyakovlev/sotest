from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryRead(BaseModel):
    name: str

    class Config:
        from_attributes = True
