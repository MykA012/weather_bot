from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from database.models.base import Base
from config.settings import settings


engine = create_async_engine(settings.db_url, echo=True)

async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession)


async def init_db() -> None:
    from database.models import user

    async with engine.begin() as conn:
        # Drop TABLES
        await conn.run_sync(Base.metadata.drop_all)
        # Create TABLES
        await conn.run_sync(Base.metadata.create_all)
