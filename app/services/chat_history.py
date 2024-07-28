from sqlalchemy.orm import Session
from app import models, schemas

def create_chat_history(db: Session, chat: schemas.ChatHistoryCreate) -> models.ChatHistory:
    db_chat = models.ChatHistory(
        user_id=chat.user_id,
        thread_id=chat.thread_id,
        user_input=chat.user_input,
        response=chat.response
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_chat_history_by_thread(db: Session, user_id: str, thread_id: str, skip: int = 0, limit: int = 10) -> list[models.ChatHistory]:
    return db.query(models.ChatHistory).filter(
        models.ChatHistory.user_id == user_id,
        models.ChatHistory.thread_id == thread_id
    ).offset(skip).limit(limit).all()
