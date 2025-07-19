from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    solicitation_number = Column(String, unique=True, index=True)
    posted_date = Column(DateTime)
    close_date = Column(DateTime)
    agency = Column(String)
    office = Column(String)
    url = Column(String)

class OpportunityCreate(BaseModel):
    id: str
    title: str
    solicitation_number: str
    posted_date: datetime
    close_date: datetime
    agency: str
    office: str
    url: str

    class Config:
        orm_mode = True

class OpportunityInDB(OpportunityCreate):
    pass
