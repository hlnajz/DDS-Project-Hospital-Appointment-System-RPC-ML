# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import assurance
import uvicorn

app = FastAPI(title="UIZ Hospital Python RPC")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in prod
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(assurance.router, prefix="/rpc", tags=["Assurance"])


