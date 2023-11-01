from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, ARRAY, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_on: Mapped[datetime] = mapped_column(default=datetime.now())


class OrganisationReview(Base):
    comment_text: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[float | None]
    category: Mapped[str | None]
    highlights: Mapped[list[str]] = mapped_column(ARRAY(String))
    organisation_id: Mapped[int] = mapped_column(ForeignKey("organisation.id"))

    __tablename__ = "organisation_review"


class SocialGroup(Base):
    social_type: Mapped[str]
    link: Mapped[str]
    organisation_id: Mapped[int] = mapped_column(ForeignKey("organisation.id"))

    __tablename__ = "social_group"


class Organisation(Base):
    full_nm: Mapped[str]
    name: Mapped[str]
    address: Mapped[str]
    longitude: Mapped[float]
    latitude: Mapped[float]
    result_rating: Mapped[float | None]
    inn: Mapped[str | None]
    phone_num: Mapped[str | None]
    email: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    org_links = relationship("SocialGroup")
    reviews = relationship("OrganisationReview")

    __tablename__ = "organisation"


class SocialAccount(Base):
    social_type: Mapped[str]
    link: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    __tablename__ = "social_account"


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(String, nullable=False, index=True)
    full_nm: Mapped[str | None]
    role: Mapped[str] = mapped_column(nullable=False)
    organisations = relationship("Organisation", backref="user", uselist=False)
    social_links = relationship("SocialAccount")

    __tablename__ = "user"
