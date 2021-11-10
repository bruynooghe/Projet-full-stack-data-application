from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Annonce(Base):
    __tablename__ = "annonces"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    surface = Column(Integer)
    location = Column(String)
    cellphone = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))