import os
import random
import string
from openai import OpenAI
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ChatHistory

def generate_threat_scenarios(description: str, user_id: str, thread_id: str) -> list[str]:
    # Get a database session
    db: Session = next(get_db())

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Query history using the retrieved database session
    history = db.query(ChatHistory).filter_by(user_id=user_id, thread_id=thread_id).all()
    history_text = "\n".join([f"User: {chat.user_input}\nAI: {chat.response}" for chat in history])
    
    prefix = "Generate threat scenarios for the following system description"
    history = f"{history_text}\nUser: {description}\nAI:"
    prompt = f"Instructions:{prefix}\n {history}"

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
        max_tokens=1000,
    )

    threat_scenarios = completion.choices[0].message.content
    
    return threat_scenarios

def generate_thread_id():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    thread_id = f"thread_{random_string}"
    return thread_id
