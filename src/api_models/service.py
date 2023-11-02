from fastapi_users import schemas
from pydantic import BaseModel


class DefaultModel(BaseModel):
    full_nm: str


class UserRead(schemas.BaseUser[int], DefaultModel):
    pass


class UserCreate(schemas.BaseUserCreate, DefaultModel):
    pass


class UserUpdate(schemas.BaseUserUpdate, DefaultModel):
    pass
