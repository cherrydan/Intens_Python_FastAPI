from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from db.settings import TEST_DATABASE_URL

##############################################
# BLOCK FOR COMMON INTERACTION WITH DATABASE  #
###############################################

# create async database engine

engine = create_async_engine(TEST_DATABASE_URL, future=True, echo=True)

# create async session for the interaction with database
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# create declarative base
Base = declarative_base()