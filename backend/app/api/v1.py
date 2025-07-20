from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from ..db import crud, models, database

router = APIRouter()

# Pydantic models for request and response validation

class NoticeBase(BaseModel):
    title: str
    agency: str
    naics: str
    deadline: datetime
    url: str
    status: str

class NoticeCreate(NoticeBase):
    notice_id: str

class Notice(NoticeBase):
    notice_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AttachmentBase(BaseModel):
    notice_id: str
    filename: str
    url: str
    content_type: str
    checksum: str
    local_path: str
    size: int
    ocr_needed: bool

class AttachmentCreate(AttachmentBase):
    pass

class Attachment(AttachmentBase):
    id: int

    class Config:
        orm_mode = True

class TextChunkBase(BaseModel):
    notice_id: str
    section: str
    content: str
    embedding: str
    vector_id: str

class TextChunkCreate(TextChunkBase):
    chunk_id: str

class TextChunk(TextChunkBase):
    chunk_id: str

    class Config:
        orm_mode = True

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints for Notices

@router.post("/notices/", response_model=Notice)
def create_notice(notice: NoticeCreate, db: Session = Depends(get_db)):
    db_notice = crud.get_notice(db, notice_id=notice.notice_id)
    if db_notice:
        raise HTTPException(status_code=400, detail="Notice ID already registered")
    return crud.create_notice(db=db, notice_data=notice.dict())

@router.get("/notices/{notice_id}", response_model=Notice)
def read_notice(notice_id: str, db: Session = Depends(get_db)):
    db_notice = crud.get_notice(db, notice_id=notice_id)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice

@router.get("/notices/", response_model=List[Notice])
def read_notices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notices = crud.get_notices(db, skip=skip, limit=limit)
    return notices

@router.put("/notices/{notice_id}", response_model=Notice)
def update_notice(notice_id: str, notice: NoticeCreate, db: Session = Depends(get_db)):
    db_notice = crud.update_notice(db, notice_id=notice_id, notice_data=notice.dict())
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice

@router.delete("/notices/{notice_id}")
def delete_notice(notice_id: str, db: Session = Depends(get_db)):
    db_notice = crud.delete_notice(db, notice_id=notice_id)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return {"message": "Notice deleted successfully"}

# API Endpoints for Attachments

@router.post("/attachments/", response_model=Attachment)
def create_attachment(attachment: AttachmentCreate, db: Session = Depends(get_db)):
    return crud.create_attachment(db=db, attachment_data=attachment.dict())

@router.get("/attachments/{attachment_id}", response_model=Attachment)
def read_attachment(attachment_id: int, db: Session = Depends(get_db)):
    db_attachment = crud.get_attachment(db, attachment_id=attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return db_attachment

@router.get("/notices/{notice_id}/attachments/", response_model=List[Attachment])
def read_attachments_by_notice_id(notice_id: str, db: Session = Depends(get_db)):
    attachments = crud.get_attachments_by_notice_id(db, notice_id=notice_id)
    return attachments

@router.put("/attachments/{attachment_id}", response_model=Attachment)
def update_attachment(attachment_id: int, attachment: AttachmentCreate, db: Session = Depends(get_db)):
    db_attachment = crud.update_attachment(db, attachment_id=attachment_id, attachment_data=attachment.dict())
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return db_attachment

@router.delete("/attachments/{attachment_id}")
def delete_attachment(attachment_id: int, db: Session = Depends(get_db)):
    db_attachment = crud.delete_attachment(db, attachment_id=attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return {"message": "Attachment deleted successfully"}

# API Endpoints for TextChunks

@router.post("/text_chunks/", response_model=TextChunk)
def create_text_chunk(text_chunk: TextChunkCreate, db: Session = Depends(get_db)):
    db_text_chunk = crud.get_text_chunk(db, chunk_id=text_chunk.chunk_id)
    if db_text_chunk:
        raise HTTPException(status_code=400, detail="Text chunk ID already registered")
    return crud.create_text_chunk(db=db, text_chunk_data=text_chunk.dict())

@router.get("/text_chunks/{chunk_id}", response_model=TextChunk)
def read_text_chunk(chunk_id: str, db: Session = Depends(get_db)):
    db_text_chunk = crud.get_text_chunk(db, chunk_id=chunk_id)
    if db_text_chunk is None:
        raise HTTPException(status_code=404, detail="Text chunk not found")
    return db_text_chunk

@router.get("/notices/{notice_id}/text_chunks/", response_model=List[TextChunk])
def read_text_chunks_by_notice_id(notice_id: str, db: Session = Depends(get_db)):
    text_chunks = crud.get_text_chunks_by_notice_id(db, notice_id=notice_id)
    return text_chunks

@router.put("/text_chunks/{chunk_id}", response_model=TextChunk)
def update_text_chunk(chunk_id: str, text_chunk: TextChunkCreate, db: Session = Depends(get_db)):
    db_text_chunk = crud.update_text_chunk(db, chunk_id=chunk_id, text_chunk_data=text_chunk.dict())
    if db_text_chunk is None:
        raise HTTPException(status_code=404, detail="Text chunk not found")
    return db_text_chunk

@router.delete("/text_chunks/{chunk_id}")
def delete_text_chunk(chunk_id: str, db: Session = Depends(get_db)):
    db_text_chunk = crud.delete_text_chunk(db, chunk_id=chunk_id)
    if db_text_chunk is None:
        raise HTTPException(status_code=404, detail="Text chunk not found")
    return {"message": "Text chunk deleted successfully"}
