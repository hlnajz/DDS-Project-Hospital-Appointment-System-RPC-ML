# app/models/schema.py
from pydantic import BaseModel
from typing import List

class AssuranceInput(BaseModel):
    age: int
    gender: str
    lifestyle: str = "average"
    chronic_conditions: int = 0

class RiskFactor(BaseModel):
    name: str
    value: float

class AssuranceOutput(BaseModel):
    suggested_plan: str
    monthly_cost: float
    coverage: str
    risk_score: float
    risk_breakdown: List[RiskFactor]
