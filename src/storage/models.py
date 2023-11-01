from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, String, ARRAY, ForeignKey
from datetime import datetime


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
    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    org_links = relationship("SocialGroup")
    reviews = relationship("OrganisationReview")

    __tablename__ = "organisation"


class SocialAccount(Base):
    social_type: Mapped[str]
    link: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))

    __tablename__ = "social_account"


class Profile(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    full_nm = Column(String)
    role: Mapped[str] = mapped_column(nullable=False)
    organisations = relationship("Organisation", backref="user", uselist=False)
    social_links = relationship("SocialAccount")
    user = relationship("User", back_populates="profile", uselist=False)

    __tablename__ = "profile"


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(String, nullable=False, index=True)
    profile = relationship("Profile", back_populates="user", uselist=False)
    __tablename__ = "user"
