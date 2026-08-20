import os
from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1 import api_router
from app.db.init_db import init_db

# Initialize Database tables
try:
    init_db()
except Exception as e:
    import os
    if os.getenv("ENVIRONMENT") == "production":
        print(f"CRITICAL: Database initialization failed in production: {e}")
        raise e
    print(f"Database initialization warning (development): {e}")

app = FastAPI(
    title="OTT Discovery API",
    description="API for the AI-Powered Social OTT Discovery & Recommendation Platform",
    version="1.0.0",
)

# CORS configuration
from app.core.config import settings

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")
