from .base import CRUDBase
from app.models.category import Category


category_crud = CRUDBase(Category)
