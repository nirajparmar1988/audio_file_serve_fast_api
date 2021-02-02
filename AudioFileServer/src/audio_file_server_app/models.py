from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from .database import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    duration_seconds = Column(Integer)
    uploaded_on = Column(DateTime, default=func.now())


class Song(BaseModel):
    __tablename__ = "song"
    # id = Column(Integer, primary_key=True, index=True)
    # duration_seconds = Column(Integer)
    # uploaded_on = Column(DateTime, default=func.now())
    name = Column(String(100), unique=True, nullable=False)


class Podcast(BaseModel):
    __tablename__ = "podcast"
    name = Column(String(100), unique=True, nullable=False)
    host = Column(String(100), nullable=False)
    participants = Column(String(100),  default='[]')


class AudioBook(BaseModel):
    __tablename__ = "audiobook"
    author = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    narrator = Column(String(100), nullable=False)
