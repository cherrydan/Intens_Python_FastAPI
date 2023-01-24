# Submenu menu model
from sqlalchemy.orm import relationship

from db.config import Base
import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Submenu(Base):
    __tablename__ = 'submenu'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("menu.id"), default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    # child = relationship("Dish")
