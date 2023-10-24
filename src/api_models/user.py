from pydantic import BaseModel, Field, EmailStr, AnyUrl
from enum import Enum


class AccountRoles(Enum, str):
    default = "default"
    business = "business"


class SocialAccountType(Enum, str):
    vk = "vk"


class SocialAccount(BaseModel):
    social_type: SocialAccountType = Field(description="Сурс социальной сети")
    link: AnyUrl = Field(description="Ссылка на социальную сеть")


class User(BaseModel):
    username: str = Field(description="Никнейм пользователя")
    email: EmailStr = Field(description="Почта пользователя")
    role: AccountRoles = Field(default=AccountRoles.default, description="Тип аккаунта пользователя")
    full_nm: str | None = Field(default=None, description="ФИО пользователя")
    social_links: list[SocialAccount] = Field(default=[], description="Ссылки на социальные сети")
