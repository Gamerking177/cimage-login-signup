import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_env
from app.routes import auth

load_env()

app = FastAPI()

origins = [
    origins.strip()
    for origins in os.getenv("CORS_ORIGINS", "").split(",")
    if origins.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
