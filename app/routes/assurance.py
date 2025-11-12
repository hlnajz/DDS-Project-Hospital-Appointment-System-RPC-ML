# app/routes/assurance.py
from fastapi import APIRouter
from app.services.assurance_logic import process_assurance
from app.models.schema import AssuranceInput, AssuranceOutput

router = APIRouter()

@router.post("/assurance", response_model=AssuranceOutput)
async def assurance_endpoint(payload: AssuranceInput):
    result = process_assurance(payload.dict())
    return result
