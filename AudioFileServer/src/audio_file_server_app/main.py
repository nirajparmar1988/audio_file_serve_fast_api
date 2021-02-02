from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src.audio_file_server_app.audio_file_factory import AudioFileFactory
from src.audio_file_server_app import models, schemas
from src.audio_file_server_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
def create_audio_file(audio_schema: schemas.AudioFileShcema, db: Session = Depends(get_db)):
    _audio_schema = audio_schema.dict()
    file_obj = AudioFileFactory.get_file_obj(_audio_schema.get('file_type'), db)
    file_data = file_obj.get_data_schema(_audio_schema.get('file_metadata'))
    return file_obj.create_file(file_data)


@app.put("/{file_type}/{file_id}/")
def update_audio_file(file_type: str, file_id: int, audio_schema: schemas.AudioFileShcema, db: Session = Depends(get_db)):
    _audio_schema = audio_schema.dict()
    file_obj = AudioFileFactory.get_file_obj(file_type, db)
    file_data = file_obj.get_data_schema(_audio_schema.get('file_metadata'), file_id)
    return file_obj.update_file(file_id, file_data)


@app.delete("/{file_type}/{file_id}/")
def delete_audio_file(file_type: str, file_id: int, db: Session = Depends(get_db)):
    file_obj = AudioFileFactory.get_file_obj(file_type, db)
    return file_obj.delete_file(file_id)


@app.get("/{file_type}/")
def get_files(file_type: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    file_obj = AudioFileFactory.get_file_obj(file_type, db)
    audio_files = file_obj.get_files(skip=skip, limit=limit)
    return audio_files


@app.get("/{file_type}/{file_id}/")
def get_file(file_type: str, file_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    file_obj = AudioFileFactory.get_file_obj(file_type, db)
    audio_file = file_obj.get_file(file_id, skip=skip, limit=limit)
    return audio_file
