from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings
from typing import Dict, List, Any, Tuple

def validate_safety_protocols(protocols: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate safety protocols"""
    errors = []
    
    # Required fields
    required_fields = ["ppe_required", "hazards", "emergency_procedures"]
    for field in required_fields:
        if field not in protocols:
            errors.append(f"Missing required field: {field}")
    
    # Validate PPE
    if "ppe_required" in protocols:
        if not isinstance(protocols["ppe_required"], list) or len(protocols["ppe_required"]) == 0:
            errors.append("PPE required must be a non-empty list")
    
    # Validate hazards
    if "hazards" in protocols:
        if not isinstance(protocols["hazards"], list) or len(protocols["hazards"]) == 0:
            errors.append("Hazards must be a non-empty list")
    
    # Validate emergency procedures
    if "emergency_procedures" in protocols:
        if not isinstance(protocols["emergency_procedures"], list) or len(protocols["emergency_procedures"]) == 0:
            errors.append("Emergency procedures must be a non-empty list")
    
    return len(errors) == 0, errors

def check_hazardous_materials(materials: List[str]) -> Dict[str, Any]:
    """Check for hazardous materials in the activity"""
    hazardous_materials = []
    
    # Define hazardous materials (simplified)
    hazardous_list = [
        "matches", "lighters", "fire", "flame", "heat_source",
        "alcohol", "ethanol", "methanol", "acetone",
        "acid", "base", "chemical", "toxic", "poison",
        "explosive", "flammable", "corrosive", "radioactive"
    ]
    
    for material in materials:
        material_lower = material.lower()
        for hazard in hazardous_list:
            if hazard in material_lower:
                hazardous_materials.append(material)
                break
    
    has_hazards = len(hazardous_materials) > 0
    
    # Determine safety level
    if len(hazardous_materials) == 0:
        safety_level = "safe"
    elif len(hazardous_materials) <= 2:
        safety_level = "moderate"
    else:
        safety_level = "high"
    
    return {
        "has_hazards": has_hazards,
        "hazardous_materials": hazardous_materials,
        "safety_level": safety_level,
        "total_materials": len(materials)
    }

def create_activity_designer_agent():
    """Create the activity designer agent"""
    
    return Agent(
        role='Hands-on Activity Designer',
        goal='Design engaging, safe, and educational hands-on activities for students',
        backstory="""You are a master science teacher and safety expert with 15 years 
        of experience in K-12 education. You excel at:
        - Creating hands-on activities that reinforce learning objectives
        - Designing activities appropriate for the available equipment
        - Ensuring all activities meet safety standards
        - Writing clear, step-by-step instructions
        - Incorporating student roles and collaboration
        - Planning for cleanup and disposal
        - Adapting activities for different class sizes and abilities""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def design_activity(topic: str, grade: str, objectives: list, equipment: list, duration: int) -> dict:
    """Generate a hands-on activity for a lesson"""
    
    agent = create_activity_designer_agent()
    
    objectives_text = "\n".join([f"- {obj['description']}" for obj in objectives])
    equipment_text = ", ".join(equipment) if equipment else "Basic classroom materials"
    
    task_description = f"""
    Design a hands-on activity for a lesson on {topic} for grade {grade} students.
    
    Lesson Details:
    - Topic: {topic}
    - Grade: {grade}
    - Duration: {duration} minutes
    - Available Equipment: {equipment_text}
    
    Learning Objectives:
    {objectives_text}
    
    Requirements:
    1. Create a hands-on activity that:
       - Reinforces the learning objectives
       - Uses available equipment (or suggest safe alternatives)
       - Is appropriate for the grade level
       - Can be completed within the time constraints
       - Engages all students in the class
    
    2. Include detailed safety considerations:
       - Required safety equipment (goggles, gloves, etc.)
       - Safety procedures and warnings
       - Emergency procedures
       - Cleanup requirements
       - Proper disposal methods
    
    3. Provide clear instructions:
       - Step-by-step procedure
       - Student roles and responsibilities
       - Group size recommendations
       - Time estimates for each step
    
    4. Consider differentiation:
       - How to support struggling students
       - Extension activities for advanced students
       - Accommodations for students with disabilities
    
    Return the results in this format:
    {{
        "activity": {{
            "title": "Activity Title",
            "description": "Brief description of the activity",
            "learning_objectives": ["list", "of", "objectives"],
            "materials": ["list", "of", "materials"],
            "safety_equipment": ["goggles", "gloves", "etc"],
            "safety_procedures": ["list", "of", "safety", "rules"],
            "steps": [
                {{
                    "step": 1,
                    "description": "Step description",
                    "time": 5,
                    "roles": ["student", "roles"]
                }}
            ],
            "cleanup": ["cleanup", "steps"],
            "disposal": ["disposal", "instructions"],
            "differentiation": {{
                "support": "How to support struggling students",
                "extension": "Extension for advanced students",
                "accommodations": "Accommodations for disabilities"
            }}
        }}
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "activity": {
            "title": "Solar Oven Construction and Testing",
            "description": "Students build and test simple solar ovens to understand solar energy conversion",
            "learning_objectives": [
                "Understand how solar energy can be converted to heat",
                "Apply engineering design principles",
                "Collect and analyze temperature data"
            ],
            "materials": [
                "Cardboard boxes (1 per group)",
                "Aluminum foil",
                "Black construction paper",
                "Thermometers",
                "Scissors",
                "Tape",
                "Rulers"
            ],
            "safety_equipment": [
                "Safety goggles (if using scissors)",
                "Gloves (optional for handling materials)"
            ],
            "safety_procedures": [
                "Use scissors carefully and only when seated",
                "Do not look directly at the sun",
                "Handle thermometers gently",
                "Wash hands after handling materials",
                "Stay in designated work areas"
            ],
            "steps": [
                {
                    "step": 1,
                    "description": "Students form groups of 3-4 and gather materials",
                    "time": 3,
                    "roles": ["Materials manager", "Recorder", "Builder", "Tester"]
                },
                {
                    "step": 2,
                    "description": "Line the inside of the box with aluminum foil",
                    "time": 5,
                    "roles": ["Builder", "Materials manager"]
                },
                {
                    "step": 3,
                    "description": "Place black paper at the bottom of the box",
                    "time": 2,
                    "roles": ["Builder"]
                },
                {
                    "step": 4,
                    "description": "Take initial temperature reading and place in sunlight",
                    "time": 3,
                    "roles": ["Tester", "Recorder"]
                },
                {
                    "step": 5,
                    "description": "Monitor temperature every 5 minutes for 20 minutes",
                    "time": 20,
                    "roles": ["Tester", "Recorder"]
                },
                {
                    "step": 6,
                    "description": "Record final temperature and clean up",
                    "time": 5,
                    "roles": ["All students"]
                }
            ],
            "cleanup": [
                "Disassemble solar ovens",
                "Return materials to designated areas",
                "Wipe down work surfaces",
                "Wash hands thoroughly"
            ],
            "disposal": [
                "Recycle cardboard boxes",
                "Reuse aluminum foil if clean",
                "Dispose of used black paper in regular trash"
            ],
            "differentiation": {
                "support": "Provide pre-cut materials and simplified instructions for struggling students",
                "extension": "Challenge advanced students to design more efficient ovens or test different materials",
                "accommodations": "Provide larger materials for students with fine motor difficulties, assign partner for students who need support"
            }
        }
    }
