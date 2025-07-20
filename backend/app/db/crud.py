from sqlalchemy.orm import Session
from . import models
from typing import List, Optional
from datetime import datetime

# CRUD operations for Notice

def create_notice(db: Session, notice_data: dict):
    db_notice = models.Notice(**notice_data)
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

def get_notice(db: Session, notice_id: str):
    return db.query(models.Notice).filter(models.Notice.notice_id == notice_id).first()

def get_notices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notice).offset(skip).limit(limit).all()

def update_notice(db: Session, notice_id: str, notice_data: dict):
    db_notice = db.query(models.Notice).filter(models.Notice.notice_id == notice_id).first()
    if db_notice:
        for key, value in notice_data.items():
            setattr(db_notice, key, value)
        db.commit()
        db.refresh(db_notice)
    return db_notice

def delete_notice(db: Session, notice_id: str):
    db_notice = db.query(models.Notice).filter(models.Notice.notice_id == notice_id).first()
    if db_notice:
        db.delete(db_notice)
        db.commit()
    return db_notice

# CRUD operations for Attachment

def create_attachment(db: Session, attachment_data: dict):
    db_attachment = models.Attachment(**attachment_data)
    db.add(db_attachment)
    db.commit()
    db.refresh(db_attachment)
    return db_attachment

def get_attachment(db: Session, attachment_id: int):
    return db.query(models.Attachment).filter(models.Attachment.id == attachment_id).first()

def get_attachments_by_notice_id(db: Session, notice_id: str):
    return db.query(models.Attachment).filter(models.Attachment.notice_id == notice_id).all()

def update_attachment(db: Session, attachment_id: int, attachment_data: dict):
    db_attachment = db.query(models.Attachment).filter(models.Attachment.id == attachment_id).first()
    if db_attachment:
        for key, value in attachment_data.items():
            setattr(db_attachment, key, value)
        db.commit()
        db.refresh(db_attachment)
    return db_attachment

def delete_attachment(db: Session, attachment_id: int):
    db_attachment = db.query(models.Attachment).filter(models.Attachment.id == attachment_id).first()
    if db_attachment:
        db.delete(db_attachment)
        db.commit()
    return db_attachment

# CRUD operations for TextChunk

def create_text_chunk(db: Session, text_chunk_data: dict):
    db_text_chunk = models.TextChunk(**text_chunk_data)
    db.add(db_text_chunk)
    db.commit()
    db.refresh(db_text_chunk)
    return db_text_chunk

def get_text_chunk(db: Session, chunk_id: str):
    return db.query(models.TextChunk).filter(models.TextChunk.chunk_id == chunk_id).first()

def get_text_chunks_by_notice_id(db: Session, notice_id: str):
    return db.query(models.TextChunk).filter(models.TextChunk.notice_id == notice_id).all()

def update_text_chunk(db: Session, chunk_id: str, text_chunk_data: dict):
    db_text_chunk = db.query(models.TextChunk).filter(models.TextChunk.chunk_id == chunk_id).first()
    if db_text_chunk:
        for key, value in text_chunk_data.items():
            setattr(db_text_chunk, key, value)
        db.commit()
        db.refresh(db_text_chunk)
    return db_text_chunk

def delete_text_chunk(db: Session, chunk_id: str):
    db_text_chunk = db.query(models.TextChunk).filter(models.TextChunk.chunk_id == chunk_id).first()
    if db_text_chunk:
        db.delete(db_text_chunk)
        db.commit()
    return db_text_chunk