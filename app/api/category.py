from fastapi import APIRouter, HTTPException, Depends

from app.crud.category import category_crud

from app.schemas.category import CategoryCreate, CategoryRead
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/category',
                   tags=['Categories'])


@router.get(
    '/',
    response_model=list[CategoryRead],
    response_model_exclude_none=True,
)
async def get_all_categories(
        session: AsyncSession = Depends(get_async_session)
):
    category = await category_crud.get_multi(session)
    return category


@router.get(
    '/{category_id}/',
    response_model=CategoryRead,
    response_model_exclude_none=True,
)
async def get_category(
        category_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    category = await category_crud.get(category_id, session)
    return category


@router.post(
    '/',
    response_model=CategoryCreate,
    response_model_exclude_none=True
)
async def create_category(
        category: CategoryCreate,
        session: AsyncSession = Depends(get_async_session)
):
    category_id = await category_crud.get_by_attribute('name',
                                                       category.name,
                                                       session)
    if category_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Подобная категория уже существует!',
        )
    new_category = await category_crud.create(category, session)
    return new_category


@router.patch('/{category_id}/',
              response_model=CategoryRead,
              response_model_exclude_none=True,)
async def partialy_update_category(
        category_id: int,
        cat_in: CategoryRead,
        session: AsyncSession = Depends(get_async_session)):
    category = await category_crud.get_by_attribute('id', category_id, session)
    category_updated = await category_crud.update(category, cat_in, session)
    return category_updated


@router.delete('/{category_id}',
               response_model=CategoryRead,
               response_model_exclude_none=True,)
async def remove_category(category_id: int,
                          session: AsyncSession = Depends(get_async_session)):
    category = await category_crud.get_by_attribute('id', category_id, session)
    deleted_cat = await category_crud.remove(category, session)
    return deleted_cat
