from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import (
    Column,
    Float,
    String,
    ARRAY,
    DateTime,
    ForeignKey,
    PrimaryKeyConstraint,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class OrganisationReview(Base):
    id = Column(String)
    comment_text = Column(String, nullable=False)
    rate = Column(Float)
    category = Column(String)
    highlights = Column(ARRAY(String), nullable=True)
    organisation_id = Column(String, ForeignKey("organisation.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "organisation_review"
    __table_args__ = [
        PrimaryKeyConstraint("id", name="organisation_review_pk"),
    ]


class SocialGroup(Base):
    id = Column(String)
    social_type = Column(String, nullable=False)
    link = Column(String, nullable=False)
    organisation_id = Column(String, ForeignKey("organisation.id"))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "social_group"
    __table_args__ = [
        PrimaryKeyConstraint("id", name="social_group_pk"),
    ]


class Organisation(Base):
    id = Column(String)
    full_nm = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    result_rating = Column(Float)
    inn = Column(String)
    phone_num = Column(String)
    email = Column(String)
    org_links = relationship("SocialGroup")
    reviews = relationship("OrganisationReview")
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now())

    __tablename__ = "organisation"
    __table_args__ = [
        PrimaryKeyConstraint("id", name="organisation_pk"),
    ]
