from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings
from typing import Dict, List, Any, Tuple

def check_reading_level(text: str, grade_level: str) -> Dict[str, Any]:
    """Check if text is appropriate for the given grade level"""
    # Simple implementation - in production, use a proper readability formula
    words = text.split()
    sentences = text.split('.')
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    
    # Grade level thresholds (simplified)
    grade_thresholds = {
        "6": {"max_sentence_length": 15, "max_word_length": 8},
        "7": {"max_sentence_length": 17, "max_word_length": 9},
        "8": {"max_sentence_length": 20, "max_word_length": 10}
    }
    
    threshold = grade_thresholds.get(grade_level, grade_thresholds["6"])
    
    is_appropriate = (avg_sentence_length <= threshold["max_sentence_length"])
    
    recommendations = []
    if not is_appropriate:
        recommendations.append("Simplify sentence structure and vocabulary")
        recommendations.append("Break complex sentences into shorter ones")
    
    return {
        "is_appropriate": is_appropriate,
        "estimated_level": "middle" if is_appropriate else "high",
        "avg_sentence_length": avg_sentence_length,
        "recommendations": recommendations
    }

def check_vocabulary_complexity(text: str, grade_level: str) -> Dict[str, Any]:
    """Check vocabulary complexity of text"""
    words = text.lower().split()
    
    # Simple complexity check based on word length
    complex_words = [word for word in words if len(word) > 8]
    complexity_score = len(complex_words) / len(words) if words else 0
    
    return {
        "complex_words": complex_words,
        "complexity_score": complexity_score,
        "total_words": len(words),
        "complex_word_count": len(complex_words)
    }

def validate_udl_flags(flags: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
    """Validate UDL flags"""
    errors = []
    
    valid_severities = ["low", "medium", "high"]
    valid_principles = ["representation", "engagement", "expression"]
    
    for flag in flags:
        # Required fields
        required_fields = ["type", "severity", "description", "suggestion", "principle"]
        for field in required_fields:
            if field not in flag:
                errors.append(f"Missing required field: {field}")
        
        # Validate severity
        if "severity" in flag and flag["severity"].lower() not in valid_severities:
            errors.append(f"Invalid severity: {flag['severity']}. Must be one of {valid_severities}")
        
        # Validate principle
        if "principle" in flag and flag["principle"].lower() not in valid_principles:
            errors.append(f"Invalid principle: {flag['principle']}. Must be one of {valid_principles}")
    
    return len(errors) == 0, errors

def create_udl_checker_agent():
    """Create the UDL checker agent"""
    
    return Agent(
        role='UDL Specialist',
        goal='Ensure lessons meet Universal Design for Learning principles and accessibility standards',
        backstory="""You are a Universal Design for Learning expert with 15 years of 
        experience in inclusive education. You excel at:
        - Identifying barriers to learning in lesson materials
        - Suggesting multiple means of representation, action, and engagement
        - Ensuring accessibility for students with diverse learning needs
        - Providing specific rewrites and accommodations
        - Checking reading levels and vocabulary complexity
        - Recommending scaffolds and supports for struggling learners
        - Ensuring cultural sensitivity and bias-free content""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def check_udl(lesson_content: dict, grade: str) -> dict:
    """Check lesson content for UDL compliance and suggest improvements"""
    
    agent = create_udl_checker_agent()
    
    # Convert lesson content to text for analysis
    lesson_text = f"""
    Topic: {lesson_content.get('topic', 'Unknown')}
    Grade: {grade}
    
    Objectives:
    {chr(10).join([f"- {obj.get('description', '')}" for obj in lesson_content.get('objectives', [])])}
    
    Activity Description:
    {lesson_content.get('activity', {}).get('activity', {}).get('description', '')}
    
    Quiz Questions:
    {chr(10).join([f"- {item.get('question', '')}" for item in lesson_content.get('quiz', {}).get('quiz_items', [])])}
    """
    
    task_description = f"""
    Analyze this lesson content for Universal Design for Learning (UDL) compliance.
    
    Lesson Content:
    {lesson_text}
    
    Requirements:
    1. Check for UDL barriers in three areas:
       - Representation (how information is presented)
       - Action & Expression (how students demonstrate learning)
       - Engagement (how students are motivated to learn)
    
    2. For each barrier found, provide:
       - Specific description of the barrier
       - Severity level (low/medium/high)
       - Suggested rewrite or accommodation
       - UDL principle being addressed
    
    3. Check reading level and vocabulary:
       - Identify complex vocabulary
       - Suggest simpler alternatives
       - Ensure grade-appropriate language
    
    4. Look for potential bias or cultural insensitivity
    
    5. Recommend specific scaffolds and supports
    
    Return the results in this format:
    {{
        "udl_flags": [
            {{
                "type": "REPRESENTATION|ACTION_EXPRESSION|ENGAGEMENT",
                "severity": "LOW|MEDIUM|HIGH",
                "description": "Description of the barrier",
                "suggestion": "Specific rewrite or accommodation",
                "principle": "UDL principle being addressed"
            }}
        ],
        "reading_level": {{
            "current_level": "estimated grade level",
            "recommendations": ["list", "of", "improvements"]
        }},
        "vocabulary": [
            {{
                "complex_word": "word",
                "simpler_alternative": "alternative",
                "context": "where it appears"
            }}
        ],
        "scaffolds": [
            "list of suggested scaffolds and supports"
        ],
        "overall_score": "percentage of UDL compliance"
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "udl_flags": [
            {
                "type": "REPRESENTATION",
                "severity": "MEDIUM",
                "description": "Solar oven construction relies heavily on visual instructions",
                "suggestion": "Add tactile models and audio descriptions for each step",
                "principle": "Multiple means of representation"
            },
            {
                "type": "ACTION_EXPRESSION",
                "severity": "LOW",
                "description": "Limited options for students to demonstrate understanding",
                "suggestion": "Offer choice of written report, oral presentation, or visual diagram",
                "principle": "Multiple means of action and expression"
            },
            {
                "type": "ENGAGEMENT",
                "severity": "LOW",
                "description": "Activity may not engage students with different interests",
                "suggestion": "Connect to students' personal experiences with energy use",
                "principle": "Multiple means of engagement"
            }
        ],
        "reading_level": {
            "current_level": "Grade 6-7",
            "recommendations": [
                "Simplify technical terms like 'capacity factor'",
                "Add more visual aids and diagrams",
                "Break complex sentences into shorter ones"
            ]
        },
        "vocabulary": [
            {
                "complex_word": "capacity factor",
                "simpler_alternative": "how much of the time it works",
                "context": "wind turbine problem"
            },
            {
                "complex_word": "kilowatt-hours",
                "simpler_alternative": "units of electricity",
                "context": "energy calculations"
            }
        ],
        "scaffolds": [
            "Provide sentence starters for written responses",
            "Use graphic organizers for data analysis",
            "Offer peer support during group activities",
            "Provide step-by-step checklists for complex tasks"
        ],
        "overall_score": "85% UDL compliant"
    }
