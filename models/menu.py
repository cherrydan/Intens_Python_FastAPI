###############################################
# BLOCK WITH DATABASE MODELS                  #
###############################################

# Main menu model
import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.config import Base


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    child1 = relationship("Submenu")
    child2 = relationship("Dish")
