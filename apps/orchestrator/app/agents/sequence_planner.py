from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings
from typing import Dict, List, Any, Tuple

def allocate_time(sections: List[Dict[str, Any]], total_time: int) -> List[Dict[str, Any]]:
    """Allocate time to sections based on priority"""
    if not sections:
        return []
    
    # Define priority weights
    priority_weights = {
        "high": 3,
        "medium": 2,
        "low": 1
    }
    
    # Calculate total weight
    total_weight = sum(priority_weights.get(section.get("priority", "medium"), 2) for section in sections)
    
    # Allocate time proportionally
    result = []
    remaining_time = total_time
    
    for i, section in enumerate(sections):
        weight = priority_weights.get(section.get("priority", "medium"), 2)
        if i == len(sections) - 1:
            # Last section gets remaining time
            duration = remaining_time
        else:
            duration = max(1, int((weight / total_weight) * total_time))
            remaining_time -= duration
        
        result.append({
            **section,
            "duration": duration
        })
    
    return result

def validate_time_budget(sections: List[Dict[str, Any]], total_time: int) -> Tuple[bool, str]:
    """Validate that sections fit within time budget"""
    allocated_time = sum(section.get("duration", 0) for section in sections)
    
    if allocated_time > total_time:
        overrun = allocated_time - total_time
        return False, f"Time budget overrun by {overrun} minutes"
    elif allocated_time < total_time * 0.8:  # Allow 20% underrun
        underrun = total_time - allocated_time
        return False, f"Time budget underutilized by {underrun} minutes"
    else:
        return True, "Time budget is valid"

def create_sequence_planner_agent():
    """Create the sequence planner agent"""
    
    return Agent(
        role='Lesson Sequence Planner',
        goal='Create detailed lesson sequences with precise timing and formative checks',
        backstory="""You are a master teacher with 20 years of classroom experience.
        You excel at:
        - Breaking down complex topics into digestible chunks
        - Allocating time effectively across lesson components
        - Designing engaging transitions between activities
        - Incorporating formative assessment opportunities
        - Ensuring lessons flow logically and maintain student engagement""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def plan_sequence(brief_data: dict, objectives: list) -> dict:
    """Generate a detailed lesson sequence with timing"""
    
    agent = create_sequence_planner_agent()
    
    objectives_text = "\n".join([f"- {obj['description']}" for obj in objectives])
    
    task_description = f"""
    Create a detailed lesson sequence for a lesson on {brief_data['topic']} 
    for grade {brief_data['gradeBand']} students.
    
    Lesson Details:
    - Topic: {brief_data['topic']}
    - Grade: {brief_data['gradeBand']}
    - Total Duration: {brief_data['periodLength'] * brief_data['days']} minutes
    - Period Length: {brief_data['periodLength']} minutes
    - Days: {brief_data['days']}
    - Class Size: {brief_data['classSize']}
    - Equipment: {', '.join(brief_data['equipment'])}
    
    Learning Objectives:
    {objectives_text}
    
    Requirements:
    1. Break the lesson into logical sections (Do Now, Introduction, Main Activity, etc.)
    2. Allocate specific time for each section
    3. Include at least one formative check per period
    4. Design smooth transitions between sections
    5. Consider the available equipment and class size
    6. Ensure the sequence supports all learning objectives
    
    Return the results in this format:
    {{
        "sections": [
            {{
                "title": "Do Now",
                "description": "Brief description of the activity",
                "duration": 5,
                "materials": ["list", "of", "materials"],
                "formative_check": "How will you check understanding?",
                "transition": "How to transition to next section"
            }}
        ],
        "total_minutes": 45,
        "formative_checks": ["list", "of", "formative", "checks"]
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "sections": [
            {
                "title": "Do Now",
                "description": "Students complete a quick warm-up activity about energy sources",
                "duration": 5,
                "materials": ["whiteboards", "markers"],
                "formative_check": "Quick poll: How many students can name 3 energy sources?",
                "transition": "Transition to main lesson with energy source discussion"
            },
            {
                "title": "Introduction",
                "description": "Introduce renewable energy concepts and today's objectives",
                "duration": 10,
                "materials": ["projector", "slides"],
                "formative_check": "Thumbs up/down: Do you understand what renewable means?",
                "transition": "Move to hands-on activity"
            },
            {
                "title": "Main Activity",
                "description": "Students build and test solar ovens",
                "duration": 25,
                "materials": ["cardboard boxes", "aluminum foil", "thermometers", "black paper"],
                "formative_check": "Check-in: Are students following safety procedures?",
                "transition": "Clean up and prepare for reflection"
            },
            {
                "title": "Wrap-up",
                "description": "Reflect on learning and connect to objectives",
                "duration": 5,
                "materials": ["exit tickets"],
                "formative_check": "Exit ticket: Name one thing you learned about solar energy",
                "transition": "Dismissal"
            }
        ],
        "total_minutes": 45,
        "formative_checks": [
            "Quick poll on energy sources",
            "Thumbs up/down understanding check",
            "Safety procedure check-in",
            "Exit ticket reflection"
        ]
    }
