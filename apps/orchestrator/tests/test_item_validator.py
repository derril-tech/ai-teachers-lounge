# Created automatically by Cursor AI (2024-08-26)
import pytest
from app.agents.quiz_builder import validate_quiz_item, validate_rubric

class TestItemValidator:
    """Test suite for quiz item validation functionality"""
    
    def test_validate_mcq_valid(self):
        """Test valid MCQ item validation"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": "Paris",
            "explanation": "Paris is the capital of France",
            "points": 1,
            "difficulty": "easy"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_mcq_insufficient_choices(self):
        """Test MCQ with insufficient choices"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Paris"],
            "correct_answer": "Paris",
            "explanation": "Paris is the capital of France",
            "points": 1,
            "difficulty": "easy"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("at least 3 choices" in error.lower() for error in errors)
    
    def test_validate_mcq_correct_answer_not_in_options(self):
        """Test MCQ with correct answer not in options"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Madrid", "Rome"],
            "correct_answer": "Paris",
            "explanation": "Paris is the capital of France",
            "points": 1,
            "difficulty": "easy"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("correct answer must be in options" in error.lower() for error in errors)
    
    def test_validate_numeric_valid(self):
        """Test valid numeric item validation"""
        item = {
            "type": "numeric",
            "question": "What is 15 + 27?",
            "correct_answer": 42,
            "tolerance": 0,
            "explanation": "15 + 27 = 42",
            "points": 2,
            "difficulty": "medium"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_numeric_missing_tolerance(self):
        """Test numeric item without tolerance"""
        item = {
            "type": "numeric",
            "question": "What is 15 + 27?",
            "correct_answer": 42,
            "explanation": "15 + 27 = 42",
            "points": 2,
            "difficulty": "medium"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("tolerance" in error.lower() for error in errors)
    
    def test_validate_short_answer_valid(self):
        """Test valid short answer item validation"""
        item = {
            "type": "short_answer",
            "question": "Name the three branches of government.",
            "correct_answer": ["executive", "legislative", "judicial"],
            "explanation": "The three branches are executive, legislative, and judicial",
            "points": 3,
            "difficulty": "hard"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_short_answer_empty_answers(self):
        """Test short answer with empty correct answers"""
        item = {
            "type": "short_answer",
            "question": "Name the three branches of government.",
            "correct_answer": [],
            "explanation": "The three branches are executive, legislative, and judicial",
            "points": 3,
            "difficulty": "hard"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("at least one correct answer" in error.lower() for error in errors)
    
    def test_validate_multi_select_valid(self):
        """Test valid multi-select item validation"""
        item = {
            "type": "multi_select",
            "question": "Which of the following are renewable energy sources?",
            "options": ["Solar", "Coal", "Wind", "Natural Gas", "Hydroelectric"],
            "correct_answer": ["Solar", "Wind", "Hydroelectric"],
            "explanation": "Solar, wind, and hydroelectric are renewable energy sources",
            "points": 2,
            "difficulty": "medium"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_multi_select_invalid_answers(self):
        """Test multi-select with invalid correct answers"""
        item = {
            "type": "multi_select",
            "question": "Which of the following are renewable energy sources?",
            "options": ["Solar", "Coal", "Wind"],
            "correct_answer": ["Solar", "Nuclear"],
            "explanation": "Solar and wind are renewable energy sources",
            "points": 2,
            "difficulty": "medium"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("correct answers must be in options" in error.lower() for error in errors)
    
    def test_validate_item_missing_required_fields(self):
        """Test item with missing required fields"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"]
            # Missing correct_answer, explanation, points, difficulty
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert len(errors) >= 4  # Should have errors for missing fields
    
    def test_validate_item_invalid_type(self):
        """Test item with invalid type"""
        item = {
            "type": "invalid_type",
            "question": "Test question",
            "correct_answer": "Test answer",
            "explanation": "Test explanation",
            "points": 1,
            "difficulty": "easy"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("invalid type" in error.lower() for error in errors)
    
    def test_validate_item_invalid_difficulty(self):
        """Test item with invalid difficulty"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": "Paris",
            "explanation": "Paris is the capital of France",
            "points": 1,
            "difficulty": "invalid_difficulty"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("invalid difficulty" in error.lower() for error in errors)
    
    def test_validate_item_invalid_points(self):
        """Test item with invalid points"""
        item = {
            "type": "mcq",
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": "Paris",
            "explanation": "Paris is the capital of France",
            "points": 0,  # Invalid: points should be > 0
            "difficulty": "easy"
        }
        
        is_valid, errors = validate_quiz_item(item)
        
        assert is_valid is False
        assert any("points must be greater than 0" in error.lower() for error in errors)

class TestRubricValidator:
    """Test suite for rubric validation functionality"""
    
    def test_validate_rubric_valid(self):
        """Test valid rubric validation"""
        rubric = {
            "question_id": 1,
            "criteria": [
                {"level": 4, "description": "Excellent response with clear reasoning"},
                {"level": 3, "description": "Good response with some reasoning"},
                {"level": 2, "description": "Basic response with minimal reasoning"},
                {"level": 1, "description": "Incomplete or incorrect response"}
            ]
        }
        
        is_valid, errors = validate_rubric(rubric)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_rubric_invalid_levels(self):
        """Test rubric with invalid levels"""
        rubric = {
            "question_id": 1,
            "criteria": [
                {"level": 5, "description": "Excellent response"},  # Invalid level
                {"level": 3, "description": "Good response"},
                {"level": 2, "description": "Basic response"},
                {"level": 1, "description": "Incomplete response"}
            ]
        }
        
        is_valid, errors = validate_rubric(rubric)
        
        assert is_valid is False
        assert any("levels must be 1-4" in error.lower() for error in errors)
    
    def test_validate_rubric_missing_levels(self):
        """Test rubric with missing levels"""
        rubric = {
            "question_id": 1,
            "criteria": [
                {"level": 4, "description": "Excellent response"},
                {"level": 2, "description": "Basic response"},
                {"level": 1, "description": "Incomplete response"}
                # Missing level 3
            ]
        }
        
        is_valid, errors = validate_rubric(rubric)
        
        assert is_valid is False
        assert any("must include all levels 1-4" in error.lower() for error in errors)
    
    def test_validate_rubric_empty_criteria(self):
        """Test rubric with empty criteria"""
        rubric = {
            "question_id": 1,
            "criteria": []
        }
        
        is_valid, errors = validate_rubric(rubric)
        
        assert is_valid is False
        assert any("at least one criterion" in error.lower() for error in errors)
    
    def test_validate_rubric_missing_description(self):
        """Test rubric with missing description"""
        rubric = {
            "question_id": 1,
            "criteria": [
                {"level": 4},  # Missing description
                {"level": 3, "description": "Good response"},
                {"level": 2, "description": "Basic response"},
                {"level": 1, "description": "Incomplete response"}
            ]
        }
        
        is_valid, errors = validate_rubric(rubric)
        
        assert is_valid is False
        assert any("description is required" in error.lower() for error in errors)
