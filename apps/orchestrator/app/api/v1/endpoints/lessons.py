from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.agents.objective_writer import write_objectives
from app.agents.sequence_planner import plan_sequence
from app.agents.quiz_builder import build_quiz
from app.agents.activity_designer import design_activity
from app.agents.timeline_historian import create_history_timeline
from app.agents.math_setter import create_math_problems
from app.agents.udl_checker import check_udl
from app.services.export_service import export_service

router = APIRouter()

class BriefData(BaseModel):
    topic: str
    gradeBand: str
    periodLength: int
    days: int
    classSize: int
    equipment: List[str]
    inclusionNotes: str

class LessonResponse(BaseModel):
    objectives: List[dict]
    sequence: dict
    quiz: dict
    activity: dict
    history: dict
    math: dict
    udl: dict
    exports: dict
    status: str

@router.post("/generate", response_model=LessonResponse)
async def generate_lesson(brief_data: BriefData):
    """Generate a complete lesson plan from brief data"""
    try:
        # Generate objectives
        objectives_result = write_objectives(brief_data.dict())
        
        # Generate sequence
        sequence_result = plan_sequence(brief_data.dict(), objectives_result["objectives"])
        
        # Generate quiz
        quiz_result = build_quiz(
            brief_data.topic,
            brief_data.gradeBand,
            objectives_result["objectives"],
            brief_data.periodLength * brief_data.days
        )
        
        # Generate activity
        activity_result = design_activity(
            brief_data.topic,
            brief_data.gradeBand,
            objectives_result["objectives"],
            brief_data.equipment,
            brief_data.periodLength * brief_data.days
        )
        
        # Generate history timeline
        history_result = create_history_timeline(
            brief_data.topic,
            brief_data.gradeBand
        )
        
        # Generate math problems
        math_result = create_math_problems(
            brief_data.topic,
            brief_data.gradeBand
        )
        
        # Check UDL compliance
        lesson_content = {
            "topic": brief_data.topic,
            "objectives": objectives_result["objectives"],
            "activity": activity_result,
            "quiz": quiz_result
        }
        udl_result = check_udl(lesson_content, brief_data.gradeBand)

        # Generate exports
        complete_lesson_data = {
            "topic": brief_data.topic,
            "objectives": objectives_result["objectives"],
            "sequence": sequence_result,
            "quiz": quiz_result,
            "activity": activity_result,
            "history": history_result,
            "math": math_result,
            "udl": udl_result
        }
        exports_result = export_service.generate_export_files(complete_lesson_data)

        return LessonResponse(
            objectives=objectives_result["objectives"],
            sequence=sequence_result,
            quiz=quiz_result,
            activity=activity_result,
            history=history_result,
            math=math_result,
            udl=udl_result,
            exports=exports_result,
            status="completed"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating lesson: {str(e)}")

@router.get("/")
async def get_lessons():
    return {"message": "Lessons endpoint - coming soon"}
