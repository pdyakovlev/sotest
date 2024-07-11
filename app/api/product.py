from fastapi import APIRouter, HTTPException, Depends

from app.crud.product import product_crud

from app.schemas.product import ProductCreate
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/product',
                   tags=['Products'])


@router.get(
    '/',
    response_model=list[ProductCreate],
    response_model_exclude_none=True,
)
async def get_all_products(
        session: AsyncSession = Depends(get_async_session)
):
    product = await product_crud.get_multi(session)
    return product


@router.get(
    '/{product_id}/',
    response_model=ProductCreate,
    response_model_exclude_none=True,
)
async def get_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    product = await product_crud.get(product_id, session)
    if product is None:
        return {"name": "No Prod",
                "category": 000}  # сделать валидатор
    return product


@router.post(
    '/',
    response_model=ProductCreate,
    response_model_exclude_none=True
)
async def create_product(
        product: ProductCreate,
        session: AsyncSession = Depends(get_async_session)
):
    product_exists = await product_crud.get_by_attribute('name',
                                                         product.name,
                                                         session)
    if product_exists is not None:
        raise HTTPException(
            status_code=422,
            detail='Подобный продукт уже существует!',
        )
    new_product = await product_crud.create(product, session)
    return new_product


@router.patch('/{product_id}/',
              response_model=ProductCreate,
              response_model_exclude_none=True,)
async def partialy_update_product(
        product_id: int,
        prod_in: ProductCreate,
        session: AsyncSession = Depends(get_async_session)):
    product = await product_crud.get(product_id, session)
    product_updated = await product_crud.update(product, prod_in, session)
    return product_updated


@router.delete('/{product_id}/',
               response_model=ProductCreate,
               response_model_exclude_none=True,)
async def remove_product(product_id: int,
                         session: AsyncSession = Depends(get_async_session)):
    product = await product_crud.get_by_attribute('id', product_id, session)
    deleted_prod = await product_crud.remove(product, session)
    return deleted_prod
