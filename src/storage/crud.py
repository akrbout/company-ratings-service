from src.storage import models
from src.storage.engine import engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from src import errors


class StorageSession:
    def __init__(self):
        self.session = async_sessionmaker(bind=engine, expire_on_commit=False)
