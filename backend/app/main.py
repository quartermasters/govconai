from fastapi import FastAPI, Depends
from app.api.v1 import api_router
from app.core.config import settings
from app.scrapers.sam_gov_scraper import SamGovScraper
from app.llm.rag import RAGPipeline
from sqlalchemy.orm import Session
from app.db.database import get_db, create_db_and_tables
from pydantic import BaseModel

class RAGQuery(BaseModel):
    query: str

app = FastAPI(
    title="GOVCONAI",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to GOVCONAI"}

@app.post(f"{settings.API_V1_STR}/scrape/sam_gov")
async def scrape_sam_gov(db: Session = Depends(get_db)):
    scraper = SamGovScraper()
    opportunities = await scraper.scrape_opportunities()
    return {"message": f"Scraped and saved {len(opportunities)} opportunities from SAM.gov"}

@app.post(f"{settings.API_V1_STR}/llm/rag")
async def run_llm_rag(rag_query: RAGQuery):
    rag_pipeline = RAGPipeline()
    response = rag_pipeline.run_rag(rag_query.query)
    return {"query": rag_query.query, "response": response}