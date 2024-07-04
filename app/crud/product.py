from .base import CRUDBase
from app.models.product import Product


category_crud = CRUDBase(Product)
