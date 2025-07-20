import httpx
from datetime import datetime
from app.db.crud import create_opportunity
from app.db.models import OpportunityCreate
from app.db.database import SessionLocal

class GrantsGovScraper:
    def __init__(self):
        self.api_url = "https://api.grants.gov/v1/api/search2"

    async def scrape_opportunities(self, keyword="health", limit=25):
        params = {"keyword": keyword}
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.api_url, json=params, headers=headers)
            print(f"Grants.gov API raw response: {response.text[:500]}")
            if response.status_code != 200:
                print(f"Grants.gov API error: {response.status_code} {response.text}")
                return []
            try:
                data = response.json()
            except Exception as e:
                print(f"Error parsing JSON: {e}")
                return []

        opps = data.get("opportunities", [])
        if not opps:
            print(f"No opportunities found in response keys: {list(data.keys())}")

        opportunities = []
        db = SessionLocal()
        for opp in opps[:limit]:
            try:
                opp_data = OpportunityCreate(
                    id=opp.get("id", ""),
                    title=opp.get("title", ""),
                    solicitation_number=opp.get("solicitationNumber", ""),
                    posted_date=datetime.strptime(opp.get("postedDate", "1970-01-01T00:00:00Z"), "%Y-%m-%dT%H:%M:%SZ"),
                    close_date=datetime.strptime(opp.get("closeDate", "1970-01-01T00:00:00Z"), "%Y-%m-%dT%H:%M:%SZ"),
                    agency=opp.get("agency", ""),
                    office=opp.get("office", ""),
                    url=opp.get("url", "")
                )
                create_opportunity(db, opp_data)
                opportunities.append(opp_data)
            except Exception as e:
                print(f"Error saving opportunity: {e}")
        db.close()
        print(f"Fetched and saved {len(opportunities)} opportunities from Grants.gov")
        return opportunities
