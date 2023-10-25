from sqlalchemy.ext.asyncio import create_async_engine
from src.settings import database_settings
from src.storage.models import Base

engine = create_async_engine(database_settings.connection_string)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
