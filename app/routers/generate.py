from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db
from app.auth import verify_token
from app.services.threat_scenario import generate_thread_id

router = APIRouter()

@router.post("/generate-threat-scenarios", response_model=schemas.ThreatScenarioResponse)
async def generate_threat_scenarios_endpoint(
    system_description: schemas.SystemDescription, 
    user: User = Depends(verify_token),
    thread_id: str = generate_thread_id()
):
    try:
        scenarios = services.generate_threat_scenarios(
            description=system_description.message, 
            user_id=user.id, 
            thread_id=thread_id
        )
        return schemas.ThreatScenarioResponse(response=scenarios)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
