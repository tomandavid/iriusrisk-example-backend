from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db
from app.auth import verify_token

router = APIRouter()

@router.get("/chat-history/", response_model=list[schemas.ChatHistory])
async def read_chat_history(
    thread_id: str,
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token)
):
    chats = services.get_chat_history_by_thread(db, user['id'], thread_id, skip=skip, limit=limit)
    return chats
