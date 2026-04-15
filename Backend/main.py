from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.insert(0, os.path.abspath("."))

# Simple test endpoint first
app = FastAPI(title="ClarityFlow")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "ClarityFlow API is running 🚀 - Backend is working!"}

@app.get("/test")
def test():
    return {"status": "ok", "message": "Test endpoint working"}
