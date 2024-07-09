from .base import CRUDBase
from app.models.product import Product


product_crud = CRUDBase(Product)
