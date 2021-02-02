from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AudioFileShcema(BaseModel):
    file_type: str
    file_metadata: dict


class SongBase(BaseModel):
    name: str
    duration_seconds: int
    uploaded_on: Optional[datetime]


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True


class SongUpdate(BaseModel):
    name: Optional[str]
    duration_seconds: Optional[int]
    uploaded_on: Optional[datetime]


class PodcastBase(BaseModel):
    name: str
    duration_seconds: int
    uploaded_on: Optional[datetime]
    host: str
    participants: str


class PodcastCreate(PodcastBase):
    pass


class PodcastUpdate(BaseModel):
    name: Optional[str]
    duration_seconds: Optional[int]
    uploaded_on: Optional[datetime]
    host: Optional[str]
    participants: Optional[str]


class Podcast(PodcastBase):
    id: int

    class Config:
        orm_mode = True


class AudioBookBase(BaseModel):
    duration_seconds: int
    uploaded_on: Optional[datetime]
    author: str
    title: str
    narrator: str


class AudioBook(AudioBookBase):
    id: int

    class Config:
        orm_mode = True


class AudioBookCreate(AudioBookBase):
    pass


class AudioBookUpdate(BaseModel):
    duration_seconds: Optional[int]
    uploaded_on: Optional[datetime]
    author: Optional[str]
    title: Optional[str]
    narrator: Optional[str]
