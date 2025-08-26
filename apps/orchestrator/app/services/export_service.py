# Created automatically by Cursor AI (2024-08-26)
from typing import Dict, List, Any, Optional
import json
import uuid
from datetime import datetime, timedelta
import hashlib
import time
from app.agents.reporter import generate_lesson_exports
from app.agents.exporter import export_lesson_materials

class ExportService:
    """Service for handling lesson exports and file management"""
    
    def __init__(self):
        self.storage_base_url = "https://storage.example.com"
        self.secret_key = "your-secret-key-here"  # In production, use environment variable
        
    def generate_export_files(self, lesson_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate all export files for a lesson"""
        try:
            # Generate document exports
            export_files = generate_lesson_exports(lesson_data)
            
            # Generate additional exports (CSV, bundle, etc.)
            additional_exports = export_lesson_materials(lesson_data, export_files)
            
            # Combine all exports
            all_exports = {**export_files, **additional_exports}
            
            # Generate file metadata
            file_metadata = self._generate_file_metadata(lesson_data, all_exports)
            
            return {
                "files": all_exports,
                "metadata": file_metadata,
                "status": "completed"
            }
            
        except Exception as e:
            return {
                "error": f"Error generating exports: {str(e)}",
                "status": "failed"
            }
    
    def _generate_file_metadata(self, lesson_data: Dict[str, Any], exports: Dict[str, Any]) -> Dict[str, Any]:
        """Generate metadata for export files"""
        topic = lesson_data.get("topic", "")
        timestamp = datetime.now()
        
        return {
            "lesson_id": str(uuid.uuid4()),
            "topic": topic,
            "generated_at": timestamp.isoformat(),
            "version": "1.0",
            "file_count": len(exports),
            "total_size_estimate": self._estimate_total_size(exports),
            "expires_at": (timestamp + timedelta(days=30)).isoformat()
        }
    
    def _estimate_total_size(self, exports: Dict[str, Any]) -> int:
        """Estimate total size of export files in bytes"""
        total_size = 0
        for content in exports.values():
            if isinstance(content, str):
                total_size += len(content.encode('utf-8'))
            elif isinstance(content, dict):
                total_size += len(json.dumps(content).encode('utf-8'))
        return total_size
    
    def create_signed_url(self, file_path: str, expiration_hours: int = 24) -> Dict[str, Any]:
        """Create a signed URL for secure file access"""
        try:
            timestamp = int(time.time()) + (expiration_hours * 3600)
            
            # Create signature
            message = f"{file_path}{timestamp}{self.secret_key}"
            signature = hashlib.sha256(message.encode()).hexdigest()[:16]
            
            signed_url = f"{self.storage_base_url}/{file_path}?expires={timestamp}&signature={signature}"
            
            return {
                "signed_url": signed_url,
                "expires_at": timestamp,
                "file_path": file_path,
                "expiration_hours": expiration_hours
            }
        except Exception as e:
            return {
                "error": f"Error creating signed URL: {str(e)}"
            }
    
    def generate_export_progress(self, lesson_id: str) -> Dict[str, Any]:
        """Generate export progress information for WebSocket updates"""
        return {
            "lesson_id": lesson_id,
            "status": "completed",
            "progress": 100,
            "files_generated": [
                "lesson_pack.pdf",
                "slides.mdx", 
                "worksheets.docx",
                "quiz.pdf",
                "gradebook.csv",
                "bundle.zip"
            ],
            "completed_at": datetime.now().isoformat()
        }
    
    def validate_export_request(self, lesson_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that lesson data is complete for export"""
        required_fields = ["topic", "objectives", "sequence", "quiz", "activity"]
        missing_fields = []
        
        for field in required_fields:
            if not lesson_data.get(field):
                missing_fields.append(field)
        
        if missing_fields:
            return {
                "valid": False,
                "missing_fields": missing_fields,
                "message": f"Missing required fields for export: {', '.join(missing_fields)}"
            }
        
        # Check for minimum requirements
        objectives = lesson_data.get("objectives", [])
        quiz_items = lesson_data.get("quiz", {}).get("quiz_items", [])
        activity_steps = lesson_data.get("activity", {}).get("activity", {}).get("steps", [])
        
        validation_issues = []
        
        if len(objectives) < 1:
            validation_issues.append("At least one learning objective required")
        
        if len(quiz_items) < 3:
            validation_issues.append("At least 3 quiz items required")
        
        if len(activity_steps) < 1:
            validation_issues.append("At least one activity step required")
        
        if validation_issues:
            return {
                "valid": False,
                "validation_issues": validation_issues,
                "message": "Lesson does not meet minimum requirements for export"
            }
        
        return {
            "valid": True,
            "message": "Lesson data is valid for export"
        }

# Global instance
export_service = ExportService()
