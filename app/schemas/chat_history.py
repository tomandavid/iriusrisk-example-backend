from pydantic import BaseModel

class ChatHistoryBase(BaseModel):
    user_id: str
    thread_id: str
    user_input: str
    response: str

class ChatHistoryCreate(ChatHistoryBase):
    pass

class ChatHistory(ChatHistoryBase):
    id: int

    class ConfigDict:
        from_attributes = True
