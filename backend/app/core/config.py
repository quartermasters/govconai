import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "GovconAI Scraper Module"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    REDIS_URL: str = os.getenv("REDIS_URL")

    # Playwright settings
    PLAYWRIGHT_BROWSER: str = os.getenv("PLAYWRIGHT_BROWSER", "chromium")
    PLAYWRIGHT_HEADLESS: bool = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() == "true"

    # S3 settings (optional)
    AWS_ACCESS_KEY_ID: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME: Optional[str] = os.getenv("AWS_S3_BUCKET_NAME")
    AWS_S3_REGION_NAME: Optional[str] = os.getenv("AWS_S3_REGION_NAME")

    # Scraping settings
    SCRAPING_THROTTLE_DELAY: float = 1.0 # seconds per request
    USER_AGENT: str = "GovconAI-Bot/1.0 https://govcon.ai/data-policy"

settings = Settings()