from sqlalchemy.orm import Session
from app.db.models import Opportunity, OpportunityCreate

def create_opportunity(db: Session, opportunity: OpportunityCreate):
    db_opportunity = Opportunity(**opportunity.dict())
    db.add(db_opportunity)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

def get_opportunity(db: Session, opportunity_id: str):
    return db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

def get_opportunities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Opportunity).offset(skip).limit(limit).all()
