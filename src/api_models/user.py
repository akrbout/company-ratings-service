from enum import Enum

from pydantic import BaseModel, Field, EmailStr, AnyUrl


class SocialAccountType(Enum):
    vk = "vk"


class SocialAccount(BaseModel):
    social_type: SocialAccountType = Field(description="Сурс социальной сети")
    link: AnyUrl = Field(description="Ссылка на социальную сеть")


class RegisterUser(BaseModel):
    email: EmailStr = Field(description="E-Mail address")
    password: str = Field(description="Password", min_length=8, max_length=32)


class User(BaseModel):
    username: str = Field(description="Никнейм пользователя", min_length=5, max_length=20)
    email: EmailStr = Field(description="Почта пользователя")
    full_nm: str | None = Field(default=None, description="ФИО пользователя")
    social_links: list[SocialAccount] = Field(default=[], description="Ссылки на социальные сети")


class RegistrateUser(User):
    password: str = Field(min_length=8, max_length=32)


class AuthUser(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=8, max_length=32)


class ProfileStatus(BaseModel):
    status: bool = Field()
    message: str = Field()


class AuthStatus(BaseModel):
    status: bool = Field()
    access_token: str | None = Field()
