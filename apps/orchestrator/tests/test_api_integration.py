# Created automatically by Cursor AI (2024-08-26)
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPIIntegration:
    """Integration tests for API endpoints"""
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert "AI Teacher's Lounge Orchestrator" in response.json()["message"]
    
    def test_lessons_endpoint(self):
        """Test lessons endpoint"""
        response = client.get("/api/v1/lessons/")
        assert response.status_code == 200
        assert "coming soon" in response.json()["message"]
    
    def test_generate_lesson_valid_data(self):
        """Test lesson generation with valid data"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 1,
            "classSize": 25,
            "equipment": ["cardboard", "aluminum_foil", "thermometers"],
            "inclusionNotes": "Include students with visual impairments"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        assert "objectives" in data
        assert "sequence" in data
        assert "quiz" in data
        assert "activity" in data
        assert "history" in data
        assert "math" in data
        assert "udl" in data
        assert "exports" in data
        assert data["status"] == "completed"
    
    def test_generate_lesson_missing_required_fields(self):
        """Test lesson generation with missing required fields"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "6"
            # Missing other required fields
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 422  # Validation error
    
    def test_generate_lesson_invalid_grade_band(self):
        """Test lesson generation with invalid grade band"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "invalid_grade",
            "periodLength": 45,
            "days": 1,
            "classSize": 25,
            "equipment": ["cardboard"],
            "inclusionNotes": "Test notes"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        # Should handle gracefully or return validation error
        assert response.status_code in [200, 422]
    
    def test_generate_lesson_large_class_size(self):
        """Test lesson generation with large class size"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 1,
            "classSize": 100,  # Large class
            "equipment": ["cardboard", "aluminum_foil"],
            "inclusionNotes": "Large class considerations"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        # Should handle large class size appropriately
        assert data["status"] == "completed"
    
    def test_generate_lesson_multiple_days(self):
        """Test lesson generation for multiple days"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 3,  # Multiple days
            "classSize": 25,
            "equipment": ["cardboard", "aluminum_foil", "thermometers"],
            "inclusionNotes": "Multi-day lesson"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "completed"
        # Should account for multiple days in planning
        assert "sequence" in data
    
    def test_generate_lesson_no_equipment(self):
        """Test lesson generation with no equipment"""
        lesson_data = {
            "topic": "Solar Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 1,
            "classSize": 25,
            "equipment": [],  # No equipment
            "inclusionNotes": "No equipment available"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "completed"
        # Should adapt to no equipment scenario
    
    def test_generate_lesson_complex_topic(self):
        """Test lesson generation with complex topic"""
        lesson_data = {
            "topic": "Quantum Mechanics and Wave-Particle Duality",
            "gradeBand": "8",
            "periodLength": 60,
            "days": 2,
            "classSize": 30,
            "equipment": ["laser_pointers", "slits", "screens"],
            "inclusionNotes": "Advanced topic for gifted students"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "completed"
        # Should handle complex topics appropriately
    
    def test_api_error_handling(self):
        """Test API error handling"""
        # Test with malformed JSON
        response = client.post("/api/v1/lessons/generate", data="invalid json")
        assert response.status_code == 422
        
        # Test with empty body
        response = client.post("/api/v1/lessons/generate", json={})
        assert response.status_code == 422
    
    def test_api_response_structure(self):
        """Test API response structure consistency"""
        lesson_data = {
            "topic": "Simple Test",
            "gradeBand": "6",
            "periodLength": 30,
            "days": 1,
            "classSize": 20,
            "equipment": ["paper", "pencils"],
            "inclusionNotes": "Basic test"
        }
        
        response = client.post("/api/v1/lessons/generate", json=lesson_data)
        assert response.status_code == 200
        
        data = response.json()
        
        # Check required fields exist
        required_fields = ["objectives", "sequence", "quiz", "activity", "history", "math", "udl", "exports", "status"]
        for field in required_fields:
            assert field in data
        
        # Check objectives structure
        assert isinstance(data["objectives"], list)
        if data["objectives"]:
            assert "description" in data["objectives"][0]
        
        # Check sequence structure
        assert isinstance(data["sequence"], dict)
        if "sections" in data["sequence"]:
            assert isinstance(data["sequence"]["sections"], list)
        
        # Check quiz structure
        assert isinstance(data["quiz"], dict)
        if "quiz_items" in data["quiz"]:
            assert isinstance(data["quiz"]["quiz_items"], list)
        
        # Check activity structure
        assert isinstance(data["activity"], dict)
        if "activity" in data["activity"]:
            assert isinstance(data["activity"]["activity"], dict)
        
        # Check exports structure
        assert isinstance(data["exports"], dict)
        assert "files" in data["exports"]
        assert "metadata" in data["exports"]
        assert "status" in data["exports"]
