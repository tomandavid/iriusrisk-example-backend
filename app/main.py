from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import generate, history
from app.database import Base, engine 

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://iriusrisk.tomandavid.com"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(generate.router)
app.include_router(history.router)
