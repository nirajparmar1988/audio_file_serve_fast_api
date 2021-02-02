from . import models, schemas


class SongFile:

    def __init__(self, db):
        self.db = db

    def get_file(self, song_id: int):
        return self.db.query(models.Song).filter(models.Song.id == song_id).first()

    def get_files(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Song).offset(skip).limit(limit).all()

    def delete_file(self, song_id: int):
        db_item = self.db.query(models.Song).filter(models.Song.id == song_id).delete()
        self.db.commit()
        return db_item

    def get_data_schema(self, data, id=None):
        if id:
            return schemas.SongUpdate(**data)
        else:
            return schemas.SongCreate(**data)

    def create_file(self, song: schemas.SongCreate):
        db_item = models.Song(**song.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update_file(self, song_id: int, song: schemas.SongUpdate):
        db_item = self.db.query(models.Song).filter(models.Song.id == song_id).one()
        for key, value in song.dict().items():
            if value is not None:
                setattr(db_item, key, value)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item


class PodcastFile:

    def __init__(self, db):
        self.db = db

    def get_data_schema(self, data, id=None):
        if id:
            return schemas.PodcastUpdate(**data)
        else:
            return schemas.PodcastCreate(**data)

    def get_file(self, podcast_id: int):
        return self.db.query(models.Podcast).filter(models.Podcast.id == podcast_id).first()

    def get_files(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Podcast).offset(skip).limit(limit).all()

    def create_file(self, podcast: schemas.PodcastCreate):
        db_item = models.Podcast(**podcast.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete_file(self, podcast_id: int):
        db_item = self.db.query(models.Podcast).filter(models.Podcast.id == podcast_id).delete()
        self.db.commit()
        return db_item

    def update_file(self, song_id: int, podcast: schemas.PodcastUpdate):
        db_item = self.db.query(models.Podcast).filter(models.Podcast.id == song_id).one()
        for key, value in podcast.dict().items():
            if value is not None:
                setattr(db_item, key, value)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item


class AudiobookFile:

    def __init__(self, db):
        self.db = db

    def get_data_schema(self, data, id= None):
        if id:
            return schemas.AudioBookUpdate(**data)
        else:
            return schemas.AudioBookCreate(**data)

    def get_files(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.AudioBook).offset(skip).limit(limit).all()

    def create_file(self, audiobook: schemas.AudioBookCreate):
        db_item = models.AudioBook(**audiobook.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete_file(self, audiobook_id: int):
        db_item = self.db.query(models.AudioBook).filter(models.AudioBook.id == audiobook_id).delete()
        self.db.commit()
        return db_item

    def update_file(self, audiobook_id: int, audiobook: schemas.AudioBookUpdate):
        db_item = self.db.query(models.AudioBook).filter(models.AudioBook.id == audiobook_id).one()
        for key, value in audiobook.dict().items():
            if value is not None:
                setattr(db_item, key, value)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item


class AudioFileFactory:

    @classmethod
    def get_file_obj(self, file_type, db):
        if file_type == "song":
            return SongFile(db)
        elif file_type == "podcast":
            return PodcastFile(db)
        elif file_type == "audiobook":
            return AudiobookFile(db)
