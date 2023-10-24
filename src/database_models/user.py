from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from datetime import datetime


class Base(DeclarativeBase):
    pass


class SocialAccount(DeclarativeBase):
    id = Column(String)
    social_type = Column(String, nullable=False)
    link = Column(String, nullable=False)
    user_id = Column(String, ForeignKey("user.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "social_account"
    __table_args__ = [
        PrimaryKeyConstraint("id", name="socal_account_pk"),
        UniqueConstraint("link"),
    ]


class User(DeclarativeBase):
    id = Column(String)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    key = Column(String, nullable=False)
    role = Column(String, nullable=False)
    full_nm = Column(String)
    social_links = relationship("SocialAccount")
    disabled = Column(Boolean, default=False)
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "user"
    __table_args__ = [
        PrimaryKeyConstraint("id", name="user_pk"),
        UniqueConstraint("username"),
        UniqueConstraint("email"),
    ]
