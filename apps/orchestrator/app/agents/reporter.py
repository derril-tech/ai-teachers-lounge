# Created automatically by Cursor AI (2024-08-26)
from crewai import Agent, Task, Crew
from langchain.tools import tool
from typing import Dict, List, Any
import json

@tool
def generate_pack_pdf(lesson_data: Dict[str, Any]) -> str:
    """Generate a comprehensive lesson pack PDF with all components"""
    try:
        # Extract lesson components
        topic = lesson_data.get("topic", "")
        objectives = lesson_data.get("objectives", [])
        sequence = lesson_data.get("sequence", {})
        quiz = lesson_data.get("quiz", {})
        activity = lesson_data.get("activity", {})
        history = lesson_data.get("history", {})
        math = lesson_data.get("math", {})
        udl = lesson_data.get("udl", {})
        
        # Generate PDF content structure
        pdf_content = {
            "title": f"Lesson Pack: {topic}",
            "sections": [
                {
                    "title": "Learning Objectives",
                    "content": objectives
                },
                {
                    "title": "Lesson Sequence",
                    "content": sequence
                },
                {
                    "title": "Assessment",
                    "content": quiz
                },
                {
                    "title": "Hands-on Activity",
                    "content": activity
                },
                {
                    "title": "Cross-Discipline Connections",
                    "content": {
                        "history": history,
                        "math": math
                    }
                },
                {
                    "title": "UDL Considerations",
                    "content": udl
                }
            ]
        }
        
        return json.dumps(pdf_content)
    except Exception as e:
        return f"Error generating pack PDF: {str(e)}"

@tool
def generate_slides_mdx(lesson_data: Dict[str, Any]) -> str:
    """Generate slides in MDX format for presentation"""
    try:
        topic = lesson_data.get("topic", "")
        objectives = lesson_data.get("objectives", [])
        sequence = lesson_data.get("sequence", {})
        
        mdx_content = f"""---
title: "{topic}"
---

# {topic}

## Learning Objectives

{chr(10).join([f"- {obj.get('description', '')}" for obj in objectives])}

## Lesson Sequence

"""
        
        if sequence.get("sections"):
            for i, section in enumerate(sequence["sections"], 1):
                mdx_content += f"""
### {i}. {section.get('title', '')}

**Duration:** {section.get('duration', 0)} minutes

{section.get('description', '')}

**Formative Check:** {section.get('formative_check', '')}

---
"""
        
        return mdx_content
    except Exception as e:
        return f"Error generating slides MDX: {str(e)}"

@tool
def generate_worksheets_docx(lesson_data: Dict[str, Any]) -> str:
    """Generate worksheets in DOCX format"""
    try:
        topic = lesson_data.get("topic", "")
        quiz = lesson_data.get("quiz", {})
        activity = lesson_data.get("activity", {})
        math = lesson_data.get("math", {})
        
        worksheet_content = {
            "title": f"Worksheets: {topic}",
            "worksheets": [
                {
                    "title": "Assessment Worksheet",
                    "type": "quiz",
                    "content": quiz.get("quiz_items", [])
                },
                {
                    "title": "Activity Worksheet",
                    "type": "activity",
                    "content": activity.get("activity", {})
                }
            ]
        }
        
        if math:
            worksheet_content["worksheets"].append({
                "title": "Math Problem Set",
                "type": "math",
                "content": math
            })
        
        return json.dumps(worksheet_content)
    except Exception as e:
        return f"Error generating worksheets DOCX: {str(e)}"

@tool
def generate_quiz_pdf(lesson_data: Dict[str, Any]) -> str:
    """Generate quiz PDF with answer key"""
    try:
        quiz = lesson_data.get("quiz", {})
        quiz_items = quiz.get("quiz_items", [])
        rubrics = quiz.get("rubrics", [])
        
        quiz_pdf_content = {
            "title": "Assessment",
            "instructions": "Complete all questions. Show your work where applicable.",
            "questions": quiz_items,
            "answer_key": {
                "answers": [item.get("correct_answer") for item in quiz_items],
                "rubrics": rubrics
            }
        }
        
        return json.dumps(quiz_pdf_content)
    except Exception as e:
        return f"Error generating quiz PDF: {str(e)}"

def create_reporter_agent() -> Agent:
    """Create the reporter agent for generating export documents"""
    return Agent(
        role="Document Reporter",
        goal="Generate high-quality, print-ready documents for lesson materials",
        backstory="""You are an expert educational document designer with years of experience 
        creating clear, engaging, and professional lesson materials. You understand the 
        importance of proper formatting, accessibility, and pedagogical best practices.""",
        tools=[generate_pack_pdf, generate_slides_mdx, generate_worksheets_docx, generate_quiz_pdf],
        verbose=True,
        allow_delegation=False
    )

def generate_lesson_exports(lesson_data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate all export documents for a lesson"""
    try:
        reporter = create_reporter_agent()
        
        # Create tasks for each export type
        pack_task = Task(
            description="Generate a comprehensive lesson pack PDF with all components",
            agent=reporter,
            expected_output="JSON structure for lesson pack PDF"
        )
        
        slides_task = Task(
            description="Generate slides in MDX format for presentation",
            agent=reporter,
            expected_output="MDX content for slides"
        )
        
        worksheets_task = Task(
            description="Generate worksheets in DOCX format",
            agent=reporter,
            expected_output="JSON structure for worksheets"
        )
        
        quiz_task = Task(
            description="Generate quiz PDF with answer key",
            agent=reporter,
            expected_output="JSON structure for quiz PDF"
        )
        
        # Create crew and execute
        crew = Crew(
            agents=[reporter],
            tasks=[pack_task, slides_task, worksheets_task, quiz_task],
            verbose=True
        )
        
        result = crew.kickoff()
        
        # Parse results
        exports = {
            "pack_pdf": result.get("pack_pdf", ""),
            "slides_mdx": result.get("slides_mdx", ""),
            "worksheets_docx": result.get("worksheets_docx", ""),
            "quiz_pdf": result.get("quiz_pdf", ""),
            "status": "completed"
        }
        
        return exports
        
    except Exception as e:
        return {
            "error": f"Error generating exports: {str(e)}",
            "status": "failed"
        }
