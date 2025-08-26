# Created automatically by Cursor AI (2024-08-26)
import pytest
from app.agents.sequence_planner import allocate_time, validate_time_budget

class TestTimeAllocator:
    """Test suite for time allocation functionality"""
    
    def test_allocate_time_basic(self):
        """Test basic time allocation"""
        total_time = 45
        sections = [
            {"title": "Introduction", "priority": "high"},
            {"title": "Main Activity", "priority": "high"},
            {"title": "Wrap-up", "priority": "medium"}
        ]
        
        result = allocate_time(sections, total_time)
        
        assert len(result) == 3
        assert sum(section["duration"] for section in result) == total_time
        assert all(section["duration"] > 0 for section in result)
    
    def test_allocate_time_with_priority(self):
        """Test time allocation with priority weighting"""
        total_time = 60
        sections = [
            {"title": "Warm-up", "priority": "low"},
            {"title": "Core Lesson", "priority": "high"},
            {"title": "Practice", "priority": "high"},
            {"title": "Review", "priority": "medium"}
        ]
        
        result = allocate_time(sections, total_time)
        
        # High priority sections should get more time
        core_lesson = next(s for s in result if s["title"] == "Core Lesson")
        practice = next(s for s in result if s["title"] == "Practice")
        warm_up = next(s for s in result if s["title"] == "Warm-up")
        
        assert core_lesson["duration"] > warm_up["duration"]
        assert practice["duration"] > warm_up["duration"]
    
    def test_validate_time_budget_valid(self):
        """Test time budget validation with valid input"""
        sections = [
            {"title": "Intro", "duration": 10},
            {"title": "Main", "duration": 25},
            {"title": "Close", "duration": 10}
        ]
        total_time = 45
        
        is_valid, message = validate_time_budget(sections, total_time)
        
        assert is_valid is True
        assert "valid" in message.lower()
    
    def test_validate_time_budget_overrun(self):
        """Test time budget validation with overrun"""
        sections = [
            {"title": "Intro", "duration": 20},
            {"title": "Main", "duration": 40},
            {"title": "Close", "duration": 10}
        ]
        total_time = 45
        
        is_valid, message = validate_time_budget(sections, total_time)
        
        assert is_valid is False
        assert "overrun" in message.lower()
    
    def test_validate_time_budget_underrun(self):
        """Test time budget validation with underrun"""
        sections = [
            {"title": "Intro", "duration": 5},
            {"title": "Main", "duration": 15},
            {"title": "Close", "duration": 5}
        ]
        total_time = 45
        
        is_valid, message = validate_time_budget(sections, total_time)
        
        assert is_valid is False
        assert "underutilized" in message.lower()
    
    def test_allocate_time_edge_cases(self):
        """Test time allocation edge cases"""
        # Test with single section
        result = allocate_time([{"title": "Single", "priority": "high"}], 30)
        assert len(result) == 1
        assert result[0]["duration"] == 30
        
        # Test with zero time
        result = allocate_time([{"title": "Test", "priority": "high"}], 0)
        assert len(result) == 1
        assert result[0]["duration"] == 0
        
        # Test with empty sections
        result = allocate_time([], 45)
        assert len(result) == 0
