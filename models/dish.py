# dish menu model

from db.config import Base
import uuid

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Submenu(Base):
    __tablename__ = 'dish'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("menu.id"), default=uuid.uuid4)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
