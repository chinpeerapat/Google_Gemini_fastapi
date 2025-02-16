import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import upload_router
from app.api.generate import generate_router
from app.api.health import health_router

app = FastAPI()

# CORS Configuration
origins_env = os.getenv("ALLOWED_ORIGINS", "http://127.0.0.1:8000")
origins = [origin.strip() for origin in origins_env.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for endpoints
app.include_router(upload_router)
app.include_router(generate_router)
app.include_router(health_router)  # Optional, for a health check endpoint
