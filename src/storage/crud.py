from src.storage import models
from src.storage.engine import engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from src import errors


class StorageSession:
    def __init__(self):
        self.session = async_sessionmaker(bind=engine, expire_on_commit=False)

    async def get_user_by_username(self, username: str) -> models.User:
        async with self.session() as session:
            statement = select(models.User).filter(
                (models.User.username == username) and (models.User.disabled is False)
            )
            result = await session.execute(statement)
            return result.scalar()

    async def get_user_by_email(self, email: str) -> models.User:
        async with self.session() as session:
            statement = select(models.User).filter(models.User.email == email and models.User.disabled is False)
            result = await session.execute(statement)
            return result.scalar()

    async def is_user_exist(self, username: str) -> bool:
        result = await self.get_user_by_username(username)
        return True if result else False

    async def is_email_exist(self, email: str) -> bool:
        result = await self.get_user_by_email(email)
        return True if result else False

    async def create_user(self, user: models.User) -> tuple:
        async with self.session() as session:
            check_user = await self.is_user_exist(user.username)
            check_email = await self.is_email_exist(user.email)
            if not check_user and not check_email:
                session.add(user)
                await session.commit()
                return True, "Created"
            else:
                return False, "User with this username or email is already exist"

    async def disable_user(self, username: str) -> bool:
        async with self.session() as session:
            user = await self.get_user_by_username(username)
            if user:
                statement = update(models.User).where(models.User.id == user.id).values(disabled=False)
                await session.execute(statement)
                await session.commit()
                return True
            else:
                raise errors.UnknowedUserError(f"User with username {username} is unknowed")
