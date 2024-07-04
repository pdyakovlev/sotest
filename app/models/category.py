from sqlalchemy import Column, String, Integer

from app.core.db import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column(String(60), unique=True, nullable=False)
