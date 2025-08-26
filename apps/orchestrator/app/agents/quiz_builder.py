from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings
from typing import Dict, List, Any, Tuple

def validate_quiz_item(item: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate a quiz item"""
    errors = []
    
    # Required fields
    required_fields = ["type", "question", "correct_answer", "explanation", "points", "difficulty"]
    for field in required_fields:
        if field not in item:
            errors.append(f"Missing required field: {field}")
    
    if errors:
        return False, errors
    
    # Validate type
    valid_types = ["mcq", "multi_select", "numeric", "short_answer"]
    if item["type"].lower() not in valid_types:
        errors.append(f"Invalid type: {item['type']}. Must be one of {valid_types}")
    
    # Validate difficulty
    valid_difficulties = ["easy", "medium", "hard"]
    if item["difficulty"].lower() not in valid_difficulties:
        errors.append(f"Invalid difficulty: {item['difficulty']}. Must be one of {valid_difficulties}")
    
    # Validate points
    if not isinstance(item["points"], (int, float)) or item["points"] <= 0:
        errors.append("Points must be greater than 0")
    
    # Type-specific validation
    if item["type"].lower() == "mcq":
        if "options" not in item:
            errors.append("MCQ items must have options")
        elif len(item["options"]) < 3:
            errors.append("MCQ items must have at least 3 choices")
        elif item["correct_answer"] not in item["options"]:
            errors.append("Correct answer must be in options")
    
    elif item["type"].lower() == "multi_select":
        if "options" not in item:
            errors.append("Multi-select items must have options")
        elif len(item["options"]) < 3:
            errors.append("Multi-select items must have at least 3 choices")
        elif not isinstance(item["correct_answer"], list):
            errors.append("Multi-select correct answer must be a list")
        elif not all(answer in item["options"] for answer in item["correct_answer"]):
            errors.append("All correct answers must be in options")
    
    elif item["type"].lower() == "numeric":
        if "tolerance" not in item:
            errors.append("Numeric items must have tolerance")
        elif not isinstance(item["tolerance"], (int, float)) or item["tolerance"] < 0:
            errors.append("Tolerance must be non-negative")
    
    elif item["type"].lower() == "short_answer":
        if not isinstance(item["correct_answer"], list):
            errors.append("Short answer correct answer must be a list")
        elif len(item["correct_answer"]) == 0:
            errors.append("Short answer must have at least one correct answer")
    
    return len(errors) == 0, errors

def validate_rubric(rubric: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate a rubric"""
    errors = []
    
    # Required fields
    if "question_id" not in rubric:
        errors.append("Missing question_id")
    if "criteria" not in rubric:
        errors.append("Missing criteria")
    
    if errors:
        return False, errors
    
    # Validate criteria
    if not isinstance(rubric["criteria"], list) or len(rubric["criteria"]) == 0:
        errors.append("Criteria must be a non-empty list")
        return False, errors
    
    # Check for all required levels (1-4)
    levels = set()
    for criterion in rubric["criteria"]:
        if "level" not in criterion:
            errors.append("Each criterion must have a level")
        elif not isinstance(criterion["level"], int) or criterion["level"] < 1 or criterion["level"] > 4:
            errors.append("Levels must be 1-4")
        else:
            levels.add(criterion["level"])
        
        if "description" not in criterion:
            errors.append("Each criterion must have a description")
    
    if levels != {1, 2, 3, 4}:
        errors.append("Rubric must include all levels 1-4")
    
    return len(errors) == 0, errors

def create_quiz_builder_agent():
    """Create the quiz builder agent"""
    
    return Agent(
        role='Assessment Specialist',
        goal='Create high-quality quiz items with answer keys and rubrics',
        backstory="""You are an assessment expert with 12 years of experience in 
        educational measurement. You excel at:
        - Creating diverse question types (MCQ, multi-select, numeric, short answer)
        - Writing plausible distractors for multiple choice questions
        - Developing clear rubrics for open-ended responses
        - Ensuring questions align with learning objectives
        - Creating questions appropriate for the grade level
        - Balancing difficulty levels across the assessment""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def build_quiz(topic: str, grade: str, objectives: list, duration: int) -> dict:
    """Generate quiz items for a lesson"""
    
    agent = create_quiz_builder_agent()
    
    objectives_text = "\n".join([f"- {obj['description']}" for obj in objectives])
    
    task_description = f"""
    Create a comprehensive quiz for a lesson on {topic} for grade {grade} students.
    
    Lesson Details:
    - Topic: {topic}
    - Grade: {grade}
    - Duration: {duration} minutes
    
    Learning Objectives:
    {objectives_text}
    
    Requirements:
    1. Create 10-12 quiz items across different types:
       - 4-5 Multiple Choice Questions (MCQ)
       - 2-3 Multi-Select Questions
       - 2-3 Numeric/Calculation Questions
       - 1-2 Short Answer Questions
       - 1 Labeling/Matching Question
    
    2. For each item:
       - Write clear, grade-appropriate questions
       - Provide correct answers and explanations
       - Include plausible distractors for MCQs
       - Assign appropriate point values
       - Tag difficulty level (easy/medium/hard)
    
    3. Create a rubric for short answer questions (1-4 scale)
    
    4. Ensure questions test different levels of understanding:
       - Recall and recognition
       - Comprehension and application
       - Analysis and evaluation
    
    Return the results in this format:
    {{
        "quiz_items": [
            {{
                "type": "MCQ",
                "question": "What is the primary source of renewable energy?",
                "options": ["A) Solar", "B) Wind", "C) Nuclear", "D) Coal"],
                "correct_answer": "A",
                "explanation": "Solar energy is the primary renewable energy source...",
                "points": 2,
                "difficulty": "easy"
            }}
        ],
        "rubrics": [
            {{
                "question_id": 1,
                "criteria": [
                    {{
                        "level": 4,
                        "description": "Complete and accurate response with examples"
                    }}
                ]
            }}
        ],
        "total_points": 25
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "quiz_items": [
            {
                "type": "MCQ",
                "question": "Which of the following is a renewable energy source?",
                "options": ["A) Coal", "B) Natural Gas", "C) Solar Power", "D) Oil"],
                "correct_answer": "C",
                "explanation": "Solar power is renewable because the sun's energy is unlimited and naturally replenished.",
                "points": 2,
                "difficulty": "easy"
            },
            {
                "type": "MCQ",
                "question": "What happens to the temperature inside a solar oven when exposed to sunlight?",
                "options": ["A) Stays the same", "B) Decreases", "C) Increases", "D) Becomes unpredictable"],
                "correct_answer": "C",
                "explanation": "Solar ovens trap and concentrate sunlight, converting it to heat energy.",
                "points": 2,
                "difficulty": "medium"
            },
            {
                "type": "MS",
                "question": "Select all the materials needed to build a basic solar oven:",
                "options": ["Cardboard box", "Aluminum foil", "Black paper", "Glass", "Plastic wrap"],
                "correct_answer": ["Cardboard box", "Aluminum foil", "Black paper"],
                "explanation": "These three materials are essential for creating the basic structure and heat absorption.",
                "points": 3,
                "difficulty": "medium"
            },
            {
                "type": "NUMERIC",
                "question": "If a solar oven reaches 150°F in 30 minutes, what is the average temperature increase per minute?",
                "options": [],
                "correct_answer": 5,
                "explanation": "150°F ÷ 30 minutes = 5°F per minute",
                "points": 3,
                "difficulty": "hard"
            },
            {
                "type": "SHORT",
                "question": "Explain why black paper is used in solar ovens.",
                "options": [],
                "correct_answer": "Black paper absorbs more sunlight and converts it to heat energy.",
                "explanation": "Black surfaces absorb more light energy than light surfaces.",
                "points": 4,
                "difficulty": "medium"
            }
        ],
        "rubrics": [
            {
                "question_id": 4,
                "criteria": [
                    {
                        "level": 4,
                        "description": "Complete explanation mentioning both absorption and heat conversion"
                    },
                    {
                        "level": 3,
                        "description": "Good explanation mentioning absorption or heat conversion"
                    },
                    {
                        "level": 2,
                        "description": "Basic explanation with some relevant information"
                    },
                    {
                        "level": 1,
                        "description": "Minimal or incorrect explanation"
                    }
                ]
            }
        ],
        "total_points": 14
    }
