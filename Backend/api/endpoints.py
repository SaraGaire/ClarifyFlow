from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from datetime import datetime
from config import settings

router = APIRouter()

@router.post("/api/v1/process")
async def process_audio(audio: UploadFile = File(...)):
    if audio.size > settings.max_upload_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    # Minimal working version for now
    return {
        "transcription": "Backend is working! This is a test transcription from your audio.",
        "tasks": [
            {
                "title": "Sample Task from Voice Dump",
                "description": "This task was extracted from your brain dump",
                "priority": 4,
                "category": "Work",
                "estimated_minutes": 45,
                "suggested_due": "today"
            }
        ],
        "session_id": "test-001",
        "clarity_score": 75
    }
