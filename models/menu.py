###############################################
# BLOCK WITH DATABASE MODELS                  #
###############################################

# Main menu model
import uuid

from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.config import Base


class Menu(Base):
    __tablename__ = 'menu'
    menu_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    submenu = relationship("Submenu")


class Submenu(Base):
    __tablename__ = 'submenu'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("menu.menu_id"), default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    dish = relationship("Dish")


class Dish(Base):
    __tablename__ = 'dish'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dish_id = Column(UUID(as_uuid=True), ForeignKey("submenu.id"), default=uuid.uuid4)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
