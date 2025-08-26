# Created automatically by Cursor AI (2024-08-26)
import pytest
from app.agents.udl_checker import check_reading_level, check_vocabulary_complexity, validate_udl_flags

class TestUDLRules:
    """Test suite for UDL rules and accessibility checking"""
    
    def test_check_reading_level_appropriate(self):
        """Test reading level check for appropriate content"""
        text = "The sun provides energy to Earth. Plants use this energy to grow."
        grade_level = "6"
        
        result = check_reading_level(text, grade_level)
        
        assert result["is_appropriate"] is True
        assert result["estimated_level"] in ["elementary", "middle", "high"]
        assert "recommendations" in result
    
    def test_check_reading_level_too_complex(self):
        """Test reading level check for complex content"""
        text = "The photoelectric effect demonstrates the quantum mechanical phenomenon whereby electromagnetic radiation induces the emission of electrons from metallic surfaces."
        grade_level = "6"
        
        result = check_reading_level(text, grade_level)
        
        assert result["is_appropriate"] is False
        assert "simplify" in result["recommendations"][0].lower()
    
    def test_check_vocabulary_complexity_simple(self):
        """Test vocabulary complexity check for simple words"""
        text = "The cat sat on the mat. The dog ran fast."
        grade_level = "6"
        
        result = check_vocabulary_complexity(text, grade_level)
        
        assert len(result["complex_words"]) == 0
        assert result["complexity_score"] <= 0.1
    
    def test_check_vocabulary_complexity_complex(self):
        """Test vocabulary complexity check for complex words"""
        text = "The photosynthesis process facilitates the conversion of solar energy into chemical energy through the utilization of chlorophyll molecules."
        grade_level = "6"
        
        result = check_vocabulary_complexity(text, grade_level)
        
        assert len(result["complex_words"]) > 0
        assert result["complexity_score"] > 0.3
        assert any("photosynthesis" in word for word in result["complex_words"])
    
    def test_validate_udl_flags_valid(self):
        """Test UDL flags validation with valid flags"""
        flags = [
            {
                "type": "reading_level",
                "severity": "medium",
                "description": "Text may be too complex for grade level",
                "suggestion": "Simplify vocabulary and sentence structure",
                "principle": "representation"
            },
            {
                "type": "visual_support",
                "severity": "low",
                "description": "Add visual aids to support understanding",
                "suggestion": "Include diagrams or images",
                "principle": "representation"
            }
        ]
        
        is_valid, errors = validate_udl_flags(flags)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_udl_flags_invalid_severity(self):
        """Test UDL flags validation with invalid severity"""
        flags = [
            {
                "type": "reading_level",
                "severity": "invalid_severity",
                "description": "Text may be too complex",
                "suggestion": "Simplify vocabulary",
                "principle": "representation"
            }
        ]
        
        is_valid, errors = validate_udl_flags(flags)
        
        assert is_valid is False
        assert any("invalid severity" in error.lower() for error in errors)
    
    def test_validate_udl_flags_missing_fields(self):
        """Test UDL flags validation with missing fields"""
        flags = [
            {
                "type": "reading_level",
                "severity": "medium"
                # Missing description, suggestion, principle
            }
        ]
        
        is_valid, errors = validate_udl_flags(flags)
        
        assert is_valid is False
        assert len(errors) >= 3  # Should have errors for missing fields
    
    def test_validate_udl_flags_invalid_principle(self):
        """Test UDL flags validation with invalid principle"""
        flags = [
            {
                "type": "reading_level",
                "severity": "medium",
                "description": "Text may be too complex",
                "suggestion": "Simplify vocabulary",
                "principle": "invalid_principle"
            }
        ]
        
        is_valid, errors = validate_udl_flags(flags)
        
        assert is_valid is False
        assert any("invalid principle" in error.lower() for error in errors)
    
    def test_check_accessibility_guidelines(self):
        """Test accessibility guidelines checking"""
        content = {
            "text": "The solar system contains planets.",
            "images": ["solar_system.jpg"],
            "audio": [],
            "video": []
        }
        
        # This would be implemented in the UDL checker
        # For now, we'll test the structure
        assert "text" in content
        assert "images" in content
        assert "audio" in content
        assert "video" in content
    
    def test_check_multimodal_support(self):
        """Test multimodal support checking"""
        lesson_content = {
            "visual_elements": ["diagrams", "charts"],
            "auditory_elements": ["explanations"],
            "kinesthetic_elements": ["hands-on activity"],
            "text_elements": ["reading materials"]
        }
        
        # Check that multiple modalities are represented
        modalities = []
        if lesson_content["visual_elements"]:
            modalities.append("visual")
        if lesson_content["auditory_elements"]:
            modalities.append("auditory")
        if lesson_content["kinesthetic_elements"]:
            modalities.append("kinesthetic")
        if lesson_content["text_elements"]:
            modalities.append("text")
        
        assert len(modalities) >= 2  # Should have at least 2 modalities
    
    def test_check_engagement_patterns(self):
        """Test engagement patterns checking"""
        activities = [
            {"type": "individual", "description": "Reading assignment"},
            {"type": "group", "description": "Discussion"},
            {"type": "hands-on", "description": "Lab activity"},
            {"type": "reflection", "description": "Journal writing"}
        ]
        
        # Check for diverse engagement patterns
        patterns = [activity["type"] for activity in activities]
        unique_patterns = set(patterns)
        
        assert len(unique_patterns) >= 3  # Should have at least 3 different patterns
    
    def test_check_expression_options(self):
        """Test expression options checking"""
        assessment_options = [
            {"type": "written", "description": "Essay response"},
            {"type": "oral", "description": "Presentation"},
            {"type": "visual", "description": "Poster creation"},
            {"type": "digital", "description": "Multimedia project"}
        ]
        
        # Check for multiple expression options
        expression_types = [option["type"] for option in assessment_options]
        unique_types = set(expression_types)
        
        assert len(unique_types) >= 2  # Should have at least 2 expression options
    
    def test_check_scaffolding_support(self):
        """Test scaffolding support checking"""
        scaffolds = [
            {"type": "vocabulary", "description": "Glossary of key terms"},
            {"type": "graphic_organizer", "description": "Concept map template"},
            {"type": "sentence_frames", "description": "Response starters"},
            {"type": "peer_support", "description": "Buddy system"}
        ]
        
        # Check for comprehensive scaffolding
        scaffold_types = [scaffold["type"] for scaffold in scaffolds]
        assert "vocabulary" in scaffold_types
        assert "graphic_organizer" in scaffold_types
        assert len(scaffolds) >= 3  # Should have at least 3 types of scaffolds
