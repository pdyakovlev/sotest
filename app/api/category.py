from fastapi import APIRouter, HTTPException, Depends

from app.crud.category import category_crud

from app.schemas.category import CategoryCreate
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post(
    '/category/',
    response_model=CategoryCreate
)
async def create_new_meeting_room(
        meeting_room: CategoryCreate,
        session: AsyncSession = Depends(get_async_session)
):
    room_id = await category_crud.get_by_attribute('name',
                                                   meeting_room.name,
                                                   session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )
    new_room = await category_crud.create(meeting_room, session)
    return new_room
