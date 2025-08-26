from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_objective_writer_agent():
    """Create the objective writer agent"""
    
    return Agent(
        role='Objective Writer',
        goal='Write clear, measurable learning objectives and success criteria for lessons',
        backstory="""You are an expert curriculum designer with 15 years of experience 
        in K-12 education. You specialize in writing learning objectives that are:
        - Specific and measurable
        - Aligned with grade-level standards
        - Student-centered and action-oriented
        - Appropriate for the time constraints given""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def write_objectives(brief_data: dict) -> dict:
    """Generate objectives and success criteria for a lesson"""
    
    agent = create_objective_writer_agent()
    
    task_description = f"""
    Create learning objectives and success criteria for a lesson on {brief_data['topic']} 
    for grade {brief_data['gradeBand']} students.
    
    Lesson Details:
    - Topic: {brief_data['topic']}
    - Grade: {brief_data['gradeBand']}
    - Duration: {brief_data['periodLength']} minutes
    - Days: {brief_data['days']}
    - Class Size: {brief_data['classSize']}
    - Equipment: {', '.join(brief_data['equipment'])}
    - Inclusion Notes: {brief_data['inclusionNotes']}
    
    Requirements:
    1. Write 3-5 clear, measurable learning objectives
    2. For each objective, provide 2-3 specific success criteria
    3. Use action verbs appropriate for the grade level
    4. Ensure objectives are achievable within the time constraints
    5. Consider the available equipment and inclusion needs
    
    Return the results in this format:
    {{
        "objectives": [
            {{
                "description": "Students will...",
                "success_criteria": [
                    "Students can...",
                    "Students demonstrate..."
                ]
            }}
        ]
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "objectives": [
            {
                "description": "Students will understand the basic principles of renewable energy",
                "success_criteria": [
                    "Students can identify three types of renewable energy sources",
                    "Students can explain how solar energy works",
                    "Students can compare renewable vs non-renewable energy"
                ]
            },
            {
                "description": "Students will design and build a simple solar-powered device",
                "success_criteria": [
                    "Students can create a working solar oven",
                    "Students can measure temperature changes",
                    "Students can explain their design choices"
                ]
            }
        ]
    }
