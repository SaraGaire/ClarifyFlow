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

    os.makedirs(settings.temp_audio_dir, exist_ok=True)
    temp_path = f"{settings.temp_audio_dir}/{datetime.now().timestamp()}_{audio.filename}"

    try:
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(audio.file, f)

        # For now, return mock data since full transcription is not working yet
        return {
            "transcription": "This is a simulated transcription. The backend is connected successfully.",
            "tasks": [
                {"title": "Finish project report", "description": "Complete the quarterly report", "priority": 5, "category": "Work", "estimated_minutes": 120, "suggested_due": "tomorrow"},
                {"title": "Buy groceries", "description": "Milk, eggs, bread", "priority": 3, "category": "Personal", "estimated_minutes": 30                {"titleay"},
                                                          "description": "Call the clinic", "priority": 4, "category": "Health", "estimated_minutes": 15, "suggested_due": "this_week"}
            ],
            "session_id": str(datetime.now().timestamp()),
            "clarity_score": 65
        }
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
