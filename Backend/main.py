from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add current directory to Python path so it can find 'api' and 'services'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.endpoints import router
from config import settings

app = FastAPI(title="ClarityFlow")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "ClarityFlow API is running 🚀"}
