from fastapi import APIRouter
from app.schemas.planner_schema import PlannerRequest
from app.agents.planner_agent import PlannerAgent

router = APIRouter(
    prefix="/planner",
    tags=["Planner"]
)

planner = PlannerAgent()


@router.post("/generate")
def generate(request: PlannerRequest):

    result = planner.generate_plan(
        subject=request.subject,
        exam_date=request.exam_date,
        hours_per_day=request.hours_per_day,
        current_level=request.current_level,
    )

    return {
        "success": True,
        "study_plan": result
    }