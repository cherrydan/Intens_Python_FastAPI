# Submenu menu model
from db.config import Base
import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class Submenu(Base):
    __tablename__ = 'submenu'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
