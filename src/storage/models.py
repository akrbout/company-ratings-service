from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import (
    Column,
    Float,
    String,
    Integer,
    Boolean,
    ARRAY,
    DateTime,
    ForeignKey,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class OrganisationReview(Base):
    id = Column(Integer)
    comment_text = Column(String, nullable=False)
    rate = Column(Float)
    category = Column(String)
    highlights = Column(ARRAY(String), nullable=True)
    organisation_id = Column(Integer, ForeignKey("organisation.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "organisation_review"
    __table_args__ = (PrimaryKeyConstraint("id", name="organisation_review_pk"),)


class SocialGroup(Base):
    id = Column(Integer)
    social_type = Column(String, nullable=False)
    link = Column(String, nullable=False)
    organisation_id = Column(Integer, ForeignKey("organisation.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "social_group"
    __table_args__ = (PrimaryKeyConstraint("id", name="social_group_pk"),)


class Organisation(Base):
    id = Column(Integer)
    full_nm = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    result_rating = Column(Float)
    inn = Column(String)
    phone_num = Column(String)
    email = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    org_links = relationship("SocialGroup")
    reviews = relationship("OrganisationReview")
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "organisation"
    __table_args__ = (PrimaryKeyConstraint("id", name="organisation_pk"),)


class SocialAccount(Base):
    id = Column(Integer)
    social_type = Column(String, nullable=False)
    link = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "social_account"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="socal_account_pk"),
        UniqueConstraint("link"),
    )


class Token(Base):
    id = Column(Integer)
    access_token = Column(String, index=True)
    expires_in = Column(DateTime(), nullable=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    __tablename__ = "token"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="token_pk"),
        UniqueConstraint("access_token"),
    )


class User(Base):
    id = Column(Integer)
    username = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    key = Column(String, nullable=False)
    role = Column(String, nullable=False)
    organisations = relationship("Organisation", backref="user", uselist=False)
    full_nm = Column(String)
    social_links = relationship("SocialAccount")
    tokens = relationship("Token")
    disabled = Column(Boolean, default=False)
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "user"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_pk"),
        UniqueConstraint("username"),
        UniqueConstraint("email"),
    )
