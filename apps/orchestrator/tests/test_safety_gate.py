# Created automatically by Cursor AI (2024-08-26)
import pytest
from typing import Dict, List, Any, Tuple
from app.agents.activity_designer import validate_safety_protocols, check_hazardous_materials

class TestSafetyGate:
    """Test suite for safety gate functionality"""
    
    def test_validate_safety_protocols_complete(self):
        """Test safety protocols validation with complete protocols"""
        protocols = {
            "ppe_required": ["safety_goggles", "gloves"],
            "hazards": ["heat", "sharp_objects"],
            "emergency_procedures": ["fire_extinguisher_location", "first_aid_kit"],
            "supervision_required": True,
            "age_restrictions": "12+"
        }
        
        is_valid, errors = validate_safety_protocols(protocols)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_safety_protocols_missing_ppe(self):
        """Test safety protocols validation with missing PPE"""
        protocols = {
            "hazards": ["heat"],
            "emergency_procedures": ["fire_extinguisher_location"],
            "supervision_required": True,
            "age_restrictions": "12+"
            # Missing ppe_required
        }
        
        is_valid, errors = validate_safety_protocols(protocols)
        
        assert is_valid is False
        assert any("ppe_required" in error.lower() for error in errors)
    
    def test_validate_safety_protocols_missing_hazards(self):
        """Test safety protocols validation with missing hazards"""
        protocols = {
            "ppe_required": ["safety_goggles"],
            "emergency_procedures": ["first_aid_kit"],
            "supervision_required": True,
            "age_restrictions": "12+"
            # Missing hazards
        }
        
        is_valid, errors = validate_safety_protocols(protocols)
        
        assert is_valid is False
        assert any("hazards" in error.lower() for error in errors)
    
    def test_validate_safety_protocols_missing_emergency(self):
        """Test safety protocols validation with missing emergency procedures"""
        protocols = {
            "ppe_required": ["safety_goggles"],
            "hazards": ["heat"],
            "supervision_required": True,
            "age_restrictions": "12+"
            # Missing emergency_procedures
        }
        
        is_valid, errors = validate_safety_protocols(protocols)
        
        assert is_valid is False
        assert any("emergency_procedures" in error.lower() for error in errors)
    
    def test_check_hazardous_materials_safe(self):
        """Test hazardous materials check with safe materials"""
        materials = ["cardboard", "aluminum_foil", "black_paper", "thermometer"]
        
        result = check_hazardous_materials(materials)
        
        assert result["has_hazards"] is False
        assert len(result["hazardous_materials"]) == 0
        assert result["safety_level"] == "safe"
    
    def test_check_hazardous_materials_hazardous(self):
        """Test hazardous materials check with hazardous materials"""
        materials = ["cardboard", "aluminum_foil", "black_paper", "thermometer", "matches", "alcohol"]
        
        result = check_hazardous_materials(materials)
        
        assert result["has_hazards"] is True
        assert len(result["hazardous_materials"]) > 0
        assert result["safety_level"] in ["moderate", "high"]
        assert "matches" in result["hazardous_materials"]
        assert "alcohol" in result["hazardous_materials"]
    
    def test_check_hazardous_materials_high_risk(self):
        """Test hazardous materials check with high-risk materials"""
        materials = ["cardboard", "aluminum_foil", "black_paper", "thermometer", "matches", "alcohol", "acid", "explosives"]
        
        result = check_hazardous_materials(materials)
        
        assert result["has_hazards"] is True
        assert result["safety_level"] == "high"
        assert len(result["hazardous_materials"]) >= 4
        assert "acid" in result["hazardous_materials"]
        assert "explosives" in result["hazardous_materials"]
    
    def test_validate_age_restrictions_appropriate(self):
        """Test age restrictions validation with appropriate restrictions"""
        activity = {
            "materials": ["cardboard", "aluminum_foil"],
            "hazards": ["heat"],
            "age_restrictions": "12+",
            "grade_level": "6"
        }
        
        is_appropriate, message = validate_age_restrictions(activity)
        
        assert is_appropriate is True
        assert "appropriate" in message.lower()
    
    def test_validate_age_restrictions_inappropriate(self):
        """Test age restrictions validation with inappropriate restrictions"""
        activity = {
            "materials": ["cardboard", "aluminum_foil", "matches"],
            "hazards": ["fire", "heat"],
            "age_restrictions": "18+",
            "grade_level": "6"
        }
        
        is_appropriate, message = validate_age_restrictions(activity)
        
        assert is_appropriate is False
        assert "inappropriate" in message.lower()
    
    def test_validate_supervision_requirements(self):
        """Test supervision requirements validation"""
        activity = {
            "hazards": ["heat", "sharp_objects"],
            "supervision_required": True,
            "supervision_ratio": "1:10"
        }
        
        is_valid, errors = validate_supervision_requirements(activity)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_supervision_requirements_missing(self):
        """Test supervision requirements validation with missing requirements"""
        activity = {
            "hazards": ["heat", "sharp_objects"],
            "supervision_required": True
            # Missing supervision_ratio
        }
        
        is_valid, errors = validate_supervision_requirements(activity)
        
        assert is_valid is False
        assert any("supervision_ratio" in error.lower() for error in errors)
    
    def test_validate_cleanup_procedures_complete(self):
        """Test cleanup procedures validation with complete procedures"""
        cleanup = {
            "materials_disposal": ["recycle_cardboard", "dispose_foil"],
            "equipment_cleaning": ["wipe_thermometers", "sanitize_surfaces"],
            "waste_management": ["separate_recyclables", "proper_disposal"],
            "area_restoration": ["return_equipment", "clean_workspace"]
        }
        
        is_valid, errors = validate_cleanup_procedures(cleanup)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_cleanup_procedures_incomplete(self):
        """Test cleanup procedures validation with incomplete procedures"""
        cleanup = {
            "materials_disposal": ["recycle_cardboard"],
            "equipment_cleaning": ["wipe_thermometers"]
            # Missing waste_management and area_restoration
        }
        
        is_valid, errors = validate_cleanup_procedures(cleanup)
        
        assert is_valid is False
        assert len(errors) >= 2  # Should have errors for missing fields
    
    def test_validate_emergency_contacts(self):
        """Test emergency contacts validation"""
        contacts = {
            "first_aid": "School nurse: 555-0123",
            "fire_department": "911",
            "poison_control": "1-800-222-1222",
            "school_office": "555-0000"
        }
        
        is_valid, errors = validate_emergency_contacts(contacts)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_emergency_contacts_missing(self):
        """Test emergency contacts validation with missing contacts"""
        contacts = {
            "first_aid": "School nurse: 555-0123"
            # Missing other emergency contacts
        }
        
        is_valid, errors = validate_emergency_contacts(contacts)
        
        assert is_valid is False
        assert len(errors) >= 2  # Should have errors for missing contacts

def validate_age_restrictions(activity: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate age restrictions for an activity"""
    grade_level = activity.get("grade_level", "")
    age_restrictions = activity.get("age_restrictions", "")
    
    # Simple validation - in production, use more sophisticated logic
    if "18+" in age_restrictions and grade_level in ["6", "7", "8"]:
        return False, "Activity has inappropriate age restrictions for grade level"
    
    return True, "Age restrictions are appropriate for grade level"

def validate_supervision_requirements(activity: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate supervision requirements"""
    errors = []
    
    if activity.get("supervision_required", False):
        if "supervision_ratio" not in activity:
            errors.append("Missing supervision ratio when supervision is required")
    
    return len(errors) == 0, errors

def validate_cleanup_procedures(cleanup: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate cleanup procedures"""
    errors = []
    
    required_fields = ["materials_disposal", "equipment_cleaning", "waste_management", "area_restoration"]
    for field in required_fields:
        if field not in cleanup:
            errors.append(f"Missing {field} procedures")
    
    return len(errors) == 0, errors

def validate_emergency_contacts(contacts: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate emergency contacts"""
    errors = []
    
    required_contacts = ["first_aid", "fire_department", "poison_control", "school_office"]
    for contact in required_contacts:
        if contact not in contacts:
            errors.append(f"Missing {contact} contact information")
    
    return len(errors) == 0, errors
