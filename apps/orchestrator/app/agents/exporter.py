# Created automatically by Cursor AI (2024-08-26)
from crewai import Agent, Task, Crew
from langchain.tools import tool
from typing import Dict, List, Any
import json
import csv
import io
import zipfile
from datetime import datetime

@tool
def generate_csv_grades(lesson_data: Dict[str, Any]) -> str:
    """Generate CSV gradebook with student roster and assessment items"""
    try:
        quiz = lesson_data.get("quiz", {})
        quiz_items = quiz.get("quiz_items", [])
        
        # Create CSV structure
        csv_data = {
            "headers": ["Student Name", "Student ID"] + [f"Q{i+1}" for i in range(len(quiz_items))] + ["Total Score", "Percentage", "Grade"],
            "rows": []
        }
        
        # Generate sample student data (in real app, this would come from the database)
        sample_students = [
            {"name": "Student 1", "id": "S001"},
            {"name": "Student 2", "id": "S002"},
            {"name": "Student 3", "id": "S003"},
            {"name": "Student 4", "id": "S004"},
            {"name": "Student 5", "id": "S005"}
        ]
        
        total_points = sum(item.get("points", 1) for item in quiz_items)
        
        for student in sample_students:
            # Generate sample scores (in real app, these would be actual student responses)
            scores = []
            for item in quiz_items:
                points = item.get("points", 1)
                # Simulate some students getting partial credit
                score = points if len(scores) % 3 != 0 else points * 0.8
                scores.append(round(score, 1))
            
            total_score = sum(scores)
            percentage = (total_score / total_points) * 100 if total_points > 0 else 0
            
            # Simple grade calculation
            if percentage >= 90:
                grade = "A"
            elif percentage >= 80:
                grade = "B"
            elif percentage >= 70:
                grade = "C"
            elif percentage >= 60:
                grade = "D"
            else:
                grade = "F"
            
            row = [student["name"], student["id"]] + scores + [total_score, round(percentage, 1), grade]
            csv_data["rows"].append(row)
        
        return json.dumps(csv_data)
    except Exception as e:
        return f"Error generating CSV grades: {str(e)}"

@tool
def generate_bundle_zip(lesson_data: Dict[str, Any], export_files: Dict[str, Any]) -> str:
    """Generate a ZIP bundle containing all lesson materials"""
    try:
        topic = lesson_data.get("topic", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        bundle_structure = {
            "bundle_name": f"lesson_{topic.replace(' ', '_').lower()}_{timestamp}",
            "files": [
                {
                    "name": "lesson_pack.pdf",
                    "type": "pdf",
                    "content": export_files.get("pack_pdf", "")
                },
                {
                    "name": "slides.mdx",
                    "type": "mdx",
                    "content": export_files.get("slides_mdx", "")
                },
                {
                    "name": "worksheets.docx",
                    "type": "docx",
                    "content": export_files.get("worksheets_docx", "")
                },
                {
                    "name": "quiz.pdf",
                    "type": "pdf",
                    "content": export_files.get("quiz_pdf", "")
                },
                {
                    "name": "gradebook.csv",
                    "type": "csv",
                    "content": export_files.get("csv_grades", "")
                },
                {
                    "name": "lesson_data.json",
                    "type": "json",
                    "content": json.dumps(lesson_data, indent=2)
                },
                {
                    "name": "README.md",
                    "type": "markdown",
                    "content": f"""# Lesson Bundle: {topic}

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Contents

- `lesson_pack.pdf` - Complete lesson plan with all components
- `slides.mdx` - Presentation slides in MDX format
- `worksheets.docx` - Student worksheets and activities
- `quiz.pdf` - Assessment with answer key
- `gradebook.csv` - Gradebook template with student roster
- `lesson_data.json` - Complete lesson data in JSON format

## Usage

1. Open `lesson_pack.pdf` for the complete lesson overview
2. Use `slides.mdx` for classroom presentations
3. Print `worksheets.docx` for student handouts
4. Use `quiz.pdf` for assessments
5. Import `gradebook.csv` into your grading system
6. Reference `lesson_data.json` for digital integration

## Notes

- All materials are designed for classroom use
- Safety protocols are included where applicable
- UDL considerations have been applied
- Cross-discipline connections are integrated
"""
                }
            ],
            "metadata": {
                "topic": topic,
                "generated_at": datetime.now().isoformat(),
                "version": "1.0",
                "total_files": 7
            }
        }
        
        return json.dumps(bundle_structure)
    except Exception as e:
        return f"Error generating bundle ZIP: {str(e)}"

@tool
def create_signed_url(file_path: str, expiration_hours: int = 24) -> str:
    """Create a signed URL for secure file access"""
    try:
        # In a real implementation, this would use AWS S3 or similar service
        # For now, we'll simulate the signed URL generation
        import hashlib
        import time
        
        timestamp = int(time.time()) + (expiration_hours * 3600)
        signature = hashlib.sha256(f"{file_path}{timestamp}".encode()).hexdigest()[:16]
        
        signed_url = f"https://storage.example.com/{file_path}?expires={timestamp}&signature={signature}"
        
        return json.dumps({
            "signed_url": signed_url,
            "expires_at": timestamp,
            "file_path": file_path
        })
    except Exception as e:
        return f"Error creating signed URL: {str(e)}"

@tool
def generate_change_log(lesson_data: Dict[str, Any], previous_version: Dict[str, Any] = None) -> str:
    """Generate a change log for lesson modifications"""
    try:
        current_version = {
            "objectives_count": len(lesson_data.get("objectives", [])),
            "sequence_sections": len(lesson_data.get("sequence", {}).get("sections", [])),
            "quiz_items": len(lesson_data.get("quiz", {}).get("quiz_items", [])),
            "activity_steps": len(lesson_data.get("activity", {}).get("activity", {}).get("steps", [])),
            "udl_flags": len(lesson_data.get("udl", {}).get("flags", []))
        }
        
        if previous_version:
            changes = []
            for key, current_value in current_version.items():
                previous_value = previous_version.get(key, 0)
                if current_value != previous_value:
                    change = current_value - previous_value
                    changes.append(f"{key}: {previous_value} → {current_value} ({change:+d})")
        else:
            changes = [f"Initial version with {value} {key}" for key, value in current_version.items()]
        
        change_log = {
            "version": "1.0",
            "timestamp": datetime.now().isoformat(),
            "changes": changes,
            "summary": f"Lesson updated with {len(changes)} modifications"
        }
        
        return json.dumps(change_log)
    except Exception as e:
        return f"Error generating change log: {str(e)}"

def create_exporter_agent() -> Agent:
    """Create the exporter agent for generating export files and bundles"""
    return Agent(
        role="Export Specialist",
        goal="Generate comprehensive export files and bundles for lesson materials",
        backstory="""You are an expert in educational technology and file management. 
        You understand the importance of creating organized, accessible, and secure 
        export packages that teachers can easily use in their classrooms.""",
        tools=[generate_csv_grades, generate_bundle_zip, create_signed_url, generate_change_log],
        verbose=True,
        allow_delegation=False
    )

def export_lesson_materials(lesson_data: Dict[str, Any], export_files: Dict[str, Any]) -> Dict[str, Any]:
    """Export all lesson materials as files and bundles"""
    try:
        exporter = create_exporter_agent()
        
        # Create tasks for export generation
        csv_task = Task(
            description="Generate CSV gradebook with student roster and assessment items",
            agent=exporter,
            expected_output="JSON structure for CSV gradebook"
        )
        
        bundle_task = Task(
            description="Generate a ZIP bundle containing all lesson materials",
            agent=exporter,
            expected_output="JSON structure for bundle ZIP"
        )
        
        change_log_task = Task(
            description="Generate a change log for lesson modifications",
            agent=exporter,
            expected_output="JSON structure for change log"
        )
        
        # Create crew and execute
        crew = Crew(
            agents=[exporter],
            tasks=[csv_task, bundle_task, change_log_task],
            verbose=True
        )
        
        result = crew.kickoff()
        
        # Generate signed URLs for each export file
        signed_urls = {}
        for file_type, content in export_files.items():
            if content:
                signed_urls[file_type] = create_signed_url(f"exports/{file_type}")
        
        exports = {
            "csv_grades": result.get("csv_grades", ""),
            "bundle_zip": result.get("bundle_zip", ""),
            "change_log": result.get("change_log", ""),
            "signed_urls": signed_urls,
            "status": "completed"
        }
        
        return exports
        
    except Exception as e:
        return {
            "error": f"Error exporting materials: {str(e)}",
            "status": "failed"
        }
