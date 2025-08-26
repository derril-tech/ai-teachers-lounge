# Created automatically by Cursor AI (2024-08-26)
"""
Runbook: Safety Incomplete
Handles scenarios where safety protocols are missing or incomplete
"""

from typing import Dict, List, Any, Tuple

class SafetyIncompleteHandler:
    """Handles incomplete safety protocol scenarios"""
    
    def __init__(self):
        self.required_safety_components = [
            "ppe_required",
            "hazards",
            "emergency_procedures",
            "supervision_required",
            "cleanup_procedures"
        ]
        
        self.safety_levels = {
            "low": ["paper", "pencils", "cardboard", "tape"],
            "medium": ["scissors", "thermometers", "fans", "small_electrical"],
            "high": ["heat_sources", "chemicals", "sharp_objects", "electrical_equipment"]
        }
    
    def detect_safety_issues(self, activity: Dict[str, Any]) -> Dict[str, Any]:
        """Detect safety issues in an activity"""
        issues = []
        missing_components = []
        
        # Check for required safety components
        for component in self.required_safety_components:
            if component not in activity or not activity[component]:
                missing_components.append(component)
        
        # Check materials for safety level
        materials = activity.get("materials", [])
        safety_level = self._determine_safety_level(materials)
        
        # Check for specific safety issues
        if safety_level == "high" and "emergency_procedures" in missing_components:
            issues.append({
                "type": "critical",
                "description": "High-risk materials require emergency procedures",
                "component": "emergency_procedures"
            })
        
        if safety_level in ["medium", "high"] and "ppe_required" in missing_components:
            issues.append({
                "type": "high",
                "description": f"{safety_level.title()}-risk activity requires PPE specification",
                "component": "ppe_required"
            })
        
        if "supervision_required" in missing_components and safety_level != "low":
            issues.append({
                "type": "medium",
                "description": "Activity requires supervision specification",
                "component": "supervision_required"
            })
        
        return {
            "safety_issues_detected": len(issues) > 0,
            "safety_level": safety_level,
            "missing_components": missing_components,
            "issues": issues,
            "block_export": len(issues) > 0,
            "recommendations": self._generate_safety_recommendations(issues, safety_level, materials)
        }
    
    def _determine_safety_level(self, materials: List[str]) -> str:
        """Determine safety level based on materials"""
        material_text = " ".join(materials).lower()
        
        # Check for high-risk materials
        high_risk_keywords = ["heat", "fire", "flame", "chemical", "acid", "base", "sharp", "blade", "electrical", "voltage"]
        if any(keyword in material_text for keyword in high_risk_keywords):
            return "high"
        
        # Check for medium-risk materials
        medium_risk_keywords = ["scissors", "thermometer", "fan", "motor", "battery", "wire"]
        if any(keyword in material_text for keyword in medium_risk_keywords):
            return "medium"
        
        return "low"
    
    def _generate_safety_recommendations(self, issues: List[Dict[str, Any]], safety_level: str, materials: List[str]) -> List[Dict[str, Any]]:
        """Generate safety recommendations"""
        recommendations = []
        
        for issue in issues:
            if issue["component"] == "ppe_required":
                recommendations.append({
                    "component": "ppe_required",
                    "description": "Add required personal protective equipment",
                    "suggestions": self._suggest_ppe(safety_level, materials),
                    "priority": "high" if safety_level in ["medium", "high"] else "medium"
                })
            
            elif issue["component"] == "hazards":
                recommendations.append({
                    "component": "hazards",
                    "description": "Identify and list potential hazards",
                    "suggestions": self._suggest_hazards(safety_level, materials),
                    "priority": "high"
                })
            
            elif issue["component"] == "emergency_procedures":
                recommendations.append({
                    "component": "emergency_procedures",
                    "description": "Specify emergency procedures",
                    "suggestions": self._suggest_emergency_procedures(safety_level),
                    "priority": "critical" if safety_level == "high" else "high"
                })
            
            elif issue["component"] == "supervision_required":
                recommendations.append({
                    "component": "supervision_required",
                    "description": "Specify supervision requirements",
                    "suggestions": self._suggest_supervision(safety_level),
                    "priority": "medium"
                })
            
            elif issue["component"] == "cleanup_procedures":
                recommendations.append({
                    "component": "cleanup_procedures",
                    "description": "Specify cleanup and disposal procedures",
                    "suggestions": self._suggest_cleanup(safety_level, materials),
                    "priority": "medium"
                })
        
        return recommendations
    
    def _suggest_ppe(self, safety_level: str, materials: List[str]) -> List[str]:
        """Suggest PPE based on safety level and materials"""
        suggestions = []
        
        if safety_level == "low":
            suggestions.append("No special PPE required")
        
        elif safety_level == "medium":
            suggestions.extend([
                "Safety goggles (if using scissors or small tools)",
                "Gloves (optional for handling materials)",
                "Closed-toe shoes recommended"
            ])
        
        elif safety_level == "high":
            suggestions.extend([
                "Safety goggles (required)",
                "Heat-resistant gloves (if using heat sources)",
                "Chemical-resistant gloves (if using chemicals)",
                "Lab coat or apron (recommended)",
                "Closed-toe shoes (required)"
            ])
        
        return suggestions
    
    def _suggest_hazards(self, safety_level: str, materials: List[str]) -> List[str]:
        """Suggest hazards based on safety level and materials"""
        suggestions = []
        
        if safety_level == "low":
            suggestions.append("Minimal hazards - standard classroom safety applies")
        
        elif safety_level == "medium":
            suggestions.extend([
                "Sharp objects (scissors, pins)",
                "Small electrical components",
                "Potential for minor cuts or scrapes",
                "Eye protection needed for cutting activities"
            ])
        
        elif safety_level == "high":
            suggestions.extend([
                "Heat sources and potential burns",
                "Chemical exposure risks",
                "Sharp objects and cutting hazards",
                "Electrical shock potential",
                "Eye and skin protection required"
            ])
        
        return suggestions
    
    def _suggest_emergency_procedures(self, safety_level: str) -> List[str]:
        """Suggest emergency procedures based on safety level"""
        suggestions = []
        
        if safety_level == "low":
            suggestions.append("Standard first aid procedures")
        
        elif safety_level == "medium":
            suggestions.extend([
                "First aid kit location",
                "Eye wash station location",
                "Emergency contact numbers",
                "Procedure for minor cuts or injuries"
            ])
        
        elif safety_level == "high":
            suggestions.extend([
                "Emergency shutdown procedures",
                "Fire extinguisher location",
                "Eye wash station and safety shower locations",
                "Emergency contact numbers (911, poison control)",
                "Evacuation procedures",
                "Chemical spill response procedures"
            ])
        
        return suggestions
    
    def _suggest_supervision(self, safety_level: str) -> List[str]:
        """Suggest supervision requirements based on safety level"""
        suggestions = []
        
        if safety_level == "low":
            suggestions.append("Standard classroom supervision")
        
        elif safety_level == "medium":
            suggestions.extend([
                "Close supervision during cutting activities",
                "Monitor use of small electrical components",
                "Supervision ratio: 1:15 recommended"
            ])
        
        elif safety_level == "high":
            suggestions.extend([
                "Direct supervision required at all times",
                "Qualified instructor must be present",
                "Supervision ratio: 1:10 maximum",
                "Additional safety officer recommended for large groups"
            ])
        
        return suggestions
    
    def _suggest_cleanup(self, safety_level: str, materials: List[str]) -> List[str]:
        """Suggest cleanup procedures based on safety level and materials"""
        suggestions = []
        
        if safety_level == "low":
            suggestions.extend([
                "Return materials to designated areas",
                "Wipe down work surfaces",
                "Wash hands thoroughly"
            ])
        
        elif safety_level == "medium":
            suggestions.extend([
                "Dispose of sharp objects properly",
                "Return electrical components to storage",
                "Clean work surfaces with appropriate cleaners",
                "Wash hands thoroughly",
                "Check for any remaining hazards"
            ])
        
        elif safety_level == "high":
            suggestions.extend([
                "Follow chemical disposal procedures",
                "Cool heat sources completely",
                "Dispose of sharp objects in designated containers",
                "Decontaminate work surfaces",
                "Wash hands and exposed skin thoroughly",
                "Check for any remaining hazards",
                "Document any incidents or near-misses"
            ])
        
        return suggestions
    
    def auto_complete_safety(self, activity: Dict[str, Any]) -> Dict[str, Any]:
        """Automatically complete missing safety components"""
        materials = activity.get("materials", [])
        safety_level = self._determine_safety_level(materials)
        
        completed_activity = {**activity}
        
        # Add missing PPE
        if "ppe_required" not in completed_activity or not completed_activity["ppe_required"]:
            completed_activity["ppe_required"] = self._suggest_ppe(safety_level, materials)
        
        # Add missing hazards
        if "hazards" not in completed_activity or not completed_activity["hazards"]:
            completed_activity["hazards"] = self._suggest_hazards(safety_level, materials)
        
        # Add missing emergency procedures
        if "emergency_procedures" not in completed_activity or not completed_activity["emergency_procedures"]:
            completed_activity["emergency_procedures"] = self._suggest_emergency_procedures(safety_level)
        
        # Add missing supervision
        if "supervision_required" not in completed_activity:
            completed_activity["supervision_required"] = safety_level != "low"
        
        # Add missing cleanup procedures
        if "cleanup_procedures" not in completed_activity or not completed_activity["cleanup_procedures"]:
            completed_activity["cleanup_procedures"] = self._suggest_cleanup(safety_level, materials)
        
        return completed_activity
    
    def validate_safety_completion(self, activity: Dict[str, Any]) -> bool:
        """Validate that all safety components are complete"""
        safety_check = self.detect_safety_issues(activity)
        return not safety_check["block_export"]

# Global handler instance
safety_handler = SafetyIncompleteHandler()
