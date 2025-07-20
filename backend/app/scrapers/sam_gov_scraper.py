import os
import json
from datetime import datetime
import httpx
from dotenv import load_dotenv
from app.db.crud import create_opportunity
from app.db.models import OpportunityCreate
from app.db.database import SessionLocal

load_dotenv()

class SamGovScraper:
    def __init__(self):
        self.api_url = "https://api.sam.gov/opportunities/v2/search"
        self.api_key = os.getenv("SAM_GOV_API_KEY", "YOUR_SAM_GOV_API_KEY")

    async def scrape_opportunities(self, limit=10):
        params = {
            "limit": limit,
            "api_key": self.api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.api_url, params=params)
            if response.status_code != 200:
                print(f"SAM.gov API error: {response.status_code} {response.text}")
                return []
            data = response.json()

        opportunities_data = []
        if "_embedded" in data and "results" in data["_embedded"]:
            for item in data["_embedded"]["results"]:
                try:
                    opportunities_data.append({
                        "id": item.get("_id"),
                        "title": item.get("title"),
                        "solicitation_number": item.get("solicitationNumber"),
                        "posted_date": datetime.strptime(item.get("postedDate"), "%Y-%m-%d"),
                        "close_date": datetime.strptime(item.get("closeDate"), "%Y-%m-%d"),
                        "agency": item.get("agency"),
                        "office": item.get("office"),
                        "url": item.get("url")
                    })
                except Exception as e:
                    print(f"Error parsing opportunity: {e}")

        db = SessionLocal()
        for opp_data in opportunities_data:
            try:
                opportunity_in = OpportunityCreate(**opp_data)
                create_opportunity(db, opportunity_in)
                print(f"Saved opportunity: {opp_data['title']}")
            except Exception as e:
                print(f"Error saving opportunity {opp_data['title']}: {e}")
        db.close()

        print(f"Found and saved {len(opportunities_data)} opportunities from SAM.gov.")
        return opportunities_data

async def main():
    scraper = SamGovScraper()
    opportunities = await scraper.scrape_opportunities()
    for opp in opportunities:
        print(json.dumps(opp, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
