from src.storage import models
from src.storage.engine import engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, insert, update, delete


class StorageSession:
    def __init__(self):
        self.session = async_sessionmaker(bind=engine, expire_on_commit=False)

    async def get_user_by_username(self, username: str) -> models.User:
        async with self.session() as session:
            statement = select(models.User).filter(models.User.username == username)
            result = await session.execute(statement)
            return result.scalar()

    async def is_user_exist(self, username: str) -> bool:
        result = await self.get_user_by_username(username)
        return True if result else None

    async def create_user(self, user: models.User) -> bool:
        async with self.session() as session:
            check_user = await self.is_user_exist(user.username)
            if check_user:
                session.add(user)
                await session.commit()
                return True
            else:
                return False
