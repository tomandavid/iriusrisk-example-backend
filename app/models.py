from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    thread_id = Column(String, index=True, nullable=False)
    user_input = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
