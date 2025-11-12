# app/services/assurance_logic.py
def process_assurance(payload: dict):
    age = payload.get("age", 30)
    gender = payload.get("gender", "male").lower()
    lifestyle = payload.get("lifestyle", "average")
    chronic_conditions = payload.get("chronic_conditions", 0)

    base_risk = 5
    if age < 25:
        base_risk += 2
    elif age < 40:
        base_risk += 5
    elif age < 60:
        base_risk += 12
    else:
        base_risk += 20

    if gender == "male":
        base_risk += 3

    if lifestyle == "sedentary":
        base_risk += 10
    elif lifestyle == "active":
        base_risk -= 3

    base_risk += chronic_conditions * 8
    risk_score = max(0, min(100, base_risk))

    if risk_score < 25:
        plan = "normal"
        coverage = "50%"
        monthly_cost = 180
    elif risk_score < 60:
        plan = "premium"
        coverage = "100%"
        monthly_cost = 365
   

    risk_factors = [
        {"name": "Age Factor", "value": age / 2},
        {"name": "Gender Factor", "value": 3 if gender == "male" else 1},
        {"name": "Lifestyle", "value": 10 if lifestyle == "sedentary" else 3 if lifestyle == "average" else 1},
        {"name": "Chronic Conditions", "value": chronic_conditions * 8},
    ]

    return {
        "suggested_plan": plan,
        "monthly_cost": monthly_cost,
        "coverage": coverage,
        "risk_score": risk_score,
        "risk_breakdown": risk_factors,
    }
