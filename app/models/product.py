from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.db import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(60), unique=False, nullable=False)
    category = Column('category', Integer, ForeignKey('category.id'))
