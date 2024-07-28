from pydantic import BaseModel

class SystemDescription(BaseModel):
    message: str

class ThreatScenarioResponse(BaseModel):
    response: str
