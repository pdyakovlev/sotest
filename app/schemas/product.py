from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import Depends
from app.models.category import Category
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.category import category_crud


class ProductCreate(BaseModel):
    name: str
    category: Optional[int]

    class Config:
        from_attributes = True

    # @field_validator('category')
    # async def check_category_exists(
    #         cls,
    #         val: int,
    #         session: AsyncSession = Depends(get_async_session)):
    #     category = await category_crud.get(val, session)
    #     if not category:
    #         raise ValueError(
    #             'Error'
    #         )
    #     return val
