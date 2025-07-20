from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Notice(Base):
    __tablename__ = "notices"

    notice_id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    agency = Column(String)
    naics = Column(String)
    deadline = Column(DateTime(timezone=True))
    url = Column(String, unique=True, index=True)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True, index=True)
    notice_id = Column(String, index=True)
    filename = Column(String)
    url = Column(String)
    content_type = Column(String)
    checksum = Column(String)
    local_path = Column(String)
    size = Column(Integer)
    ocr_needed = Column(Boolean, default=False)

class TextChunk(Base):
    __tablename__ = "text_chunks"

    chunk_id = Column(String, primary_key=True, index=True)
    notice_id = Column(String, index=True)
    section = Column(String)
    content = Column(Text)
    embedding = Column(Text) # Store as string for now, will convert to vector later
    vector_id = Column(String)