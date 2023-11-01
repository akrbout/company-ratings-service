from enum import Enum

from pydantic import BaseModel, Field, AnyUrl


class OrganisationReview(BaseModel):
    comment_text: str | None = Field(default=None, description="Отзыв на организацию")
    rate: float = Field(description="Оценка организации")
    category: str | None = Field(description="Категория отзыва")
    highlights: list[str] = Field(default=[], description="Хайлайты в тексте отзыва")


class SocialGroupType(Enum, str):
    vk = "vk"
    ok = "ok"
    instagram = "instagram"
    youtube = "youtube"
    other = "other"


class SocialGroup(Enum, str):
    social_type: SocialGroupType = Field(default=SocialGroupType.other, description="Сурс социальной сети")
    link: AnyUrl = Field(description="Ссылка на социальную сеть")


class Organisation(BaseModel):
    full_nm: str = Field(description="Полное название организации")
    name: str = Field(description="Название организации")
    address: str = Field(description="Адрес организации")
    longitude: float = Field(description="Долгота")
    latitude: float = Field(description="Широта")
    result_rating: float | None = Field(default=None, description="Рейтинг организации")
    inn: str | None = Field(default=None, description="ИНН организации")
    phone_num: str | None = Field(default=None, description="Номер телефона организации")
    email: str | None = Field(default=None, description="Электронная почта организации")
    org_links: list[SocialGroup] = Field(default=[], description="Ссылки на группы в социальных сетях/лендингах")
    reviews: list[OrganisationReview] = Field(default=[], description="Отзывы на организацию")
