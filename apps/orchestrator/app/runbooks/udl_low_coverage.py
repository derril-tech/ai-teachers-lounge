# Created automatically by Cursor AI (2024-08-26)
"""
Runbook: UDL Low Coverage
Handles scenarios where Universal Design for Learning coverage is insufficient
"""

from typing import Dict, List, Any, Tuple

class UDLLowCoverageHandler:
    """Handles low UDL coverage scenarios"""
    
    def __init__(self):
        self.udl_principles = ["representation", "engagement", "expression"]
        self.minimum_coverage_score = 70  # 70% minimum UDL compliance
        self.critical_udl_flags = [
            "reading_level",
            "vocabulary_complexity",
            "visual_support",
            "engagement_options",
            "expression_choices"
        ]
    
    def detect_udl_issues(self, udl_data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect UDL coverage issues"""
        issues = []
        missing_components = []
        
        # Check overall UDL score
        overall_score = self._extract_score(udl_data.get("overall_score", "0%"))
        
        if overall_score < self.minimum_coverage_score:
            issues.append({
                "type": "coverage",
                "description": f"Overall UDL coverage ({overall_score}%) below minimum threshold ({self.minimum_coverage_score}%)",
                "severity": "high" if overall_score < 50 else "medium"
            })
        
        # Check UDL flags
        udl_flags = udl_data.get("udl_flags", [])
        flag_types = [flag.get("type", "").lower() for flag in udl_flags]
        
        for principle in self.udl_principles:
            if principle not in flag_types:
                missing_components.append(principle)
                issues.append({
                    "type": "principle",
                    "description": f"Missing UDL principle: {principle}",
                    "severity": "medium"
                })
        
        # Check for critical flags
        critical_issues = [flag for flag in udl_flags if flag.get("severity", "").lower() == "high"]
        if critical_issues:
            issues.extend([
                {
                    "type": "critical",
                    "description": f"Critical UDL issue: {issue.get('description', '')}",
                    "severity": "critical",
                    "component": issue.get("type", "")
                }
                for issue in critical_issues
            ])
        
        # Check reading level
        reading_level = udl_data.get("reading_level", {})
        if reading_level and reading_level.get("current_level", ""):
            current_level = reading_level.get("current_level", "")
            if "grade" in current_level.lower():
                grade_num = self._extract_grade_number(current_level)
                if grade_num and grade_num > 8:  # High school level
                    issues.append({
                        "type": "reading_level",
                        "description": f"Reading level ({current_level}) may be too complex for target grade",
                        "severity": "medium"
                    })
        
        # Check vocabulary complexity
        vocabulary = udl_data.get("vocabulary", [])
        if vocabulary and len(vocabulary) > 5:
            issues.append({
                "type": "vocabulary",
                "description": f"High vocabulary complexity ({len(vocabulary)} complex words identified)",
                "severity": "medium"
            })
        
        return {
            "udl_issues_detected": len(issues) > 0,
            "overall_score": overall_score,
            "missing_components": missing_components,
            "issues": issues,
            "recommendations": self._generate_udl_recommendations(issues, udl_data)
        }
    
    def _extract_score(self, score_string: str) -> float:
        """Extract numeric score from string like '85% UDL compliant'"""
        try:
            # Extract percentage
            if "%" in score_string:
                return float(score_string.split("%")[0])
            # Extract number
            import re
            numbers = re.findall(r'\d+', score_string)
            if numbers:
                return float(numbers[0])
            return 0.0
        except:
            return 0.0
    
    def _extract_grade_number(self, grade_string: str) -> int:
        """Extract grade number from string like 'Grade 6-7'"""
        try:
            import re
            numbers = re.findall(r'\d+', grade_string)
            if numbers:
                return int(numbers[0])
            return None
        except:
            return None
    
    def _generate_udl_recommendations(self, issues: List[Dict[str, Any]], udl_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate UDL improvement recommendations"""
        recommendations = []
        
        for issue in issues:
            if issue["type"] == "coverage":
                recommendations.append({
                    "strategy": "apply_suggested_rewrites",
                    "description": "Apply suggested UDL rewrites to improve accessibility",
                    "priority": "high",
                    "implementation": "Use UDL checker suggestions to modify content"
                })
            
            elif issue["type"] == "principle":
                principle = issue.get("description", "").split(": ")[-1]
                recommendations.append({
                    "strategy": f"add_{principle}_support",
                    "description": f"Add {principle} support to lesson materials",
                    "priority": "medium",
                    "implementation": self._get_principle_implementation(principle)
                })
            
            elif issue["type"] == "reading_level":
                recommendations.append({
                    "strategy": "simplify_language",
                    "description": "Simplify language and sentence structure",
                    "priority": "medium",
                    "implementation": [
                        "Break complex sentences into shorter ones",
                        "Replace complex vocabulary with simpler alternatives",
                        "Add definitions for technical terms"
                    ]
                })
            
            elif issue["type"] == "vocabulary":
                recommendations.append({
                    "strategy": "add_vocabulary_support",
                    "description": "Add vocabulary support and definitions",
                    "priority": "medium",
                    "implementation": [
                        "Create glossary of key terms",
                        "Add inline definitions",
                        "Provide vocabulary preview activities"
                    ]
                })
            
            elif issue["type"] == "critical":
                recommendations.append({
                    "strategy": "address_critical_issue",
                    "description": f"Address critical UDL issue: {issue.get('description', '')}",
                    "priority": "critical",
                    "implementation": "Immediate attention required - review and revise content"
                })
        
        return recommendations
    
    def _get_principle_implementation(self, principle: str) -> List[str]:
        """Get implementation suggestions for UDL principles"""
        implementations = {
            "representation": [
                "Add visual aids (diagrams, charts, images)",
                "Provide audio alternatives for text",
                "Use multiple formats for presenting information",
                "Add captions and transcripts for multimedia"
            ],
            "engagement": [
                "Offer choice in learning activities",
                "Connect content to student interests",
                "Provide multiple engagement options",
                "Include collaborative and individual work options"
            ],
            "expression": [
                "Offer multiple ways to demonstrate learning",
                "Provide templates and scaffolds",
                "Allow choice in assessment formats",
                "Include both written and oral response options"
            ]
        }
        
        return implementations.get(principle, ["Review and enhance accessibility features"])
    
    def apply_suggested_rewrites(self, udl_data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply suggested UDL rewrites to improve coverage"""
        improved_data = {**udl_data}
        
        # Apply vocabulary suggestions
        vocabulary = udl_data.get("vocabulary", [])
        if vocabulary:
            improved_data["vocabulary_support"] = {
                "glossary": [{"term": item["complex_word"], "definition": item["simpler_alternative"]} for item in vocabulary],
                "inline_definitions": True,
                "preview_activity": "Vocabulary matching game"
            }
        
        # Apply reading level suggestions
        reading_level = udl_data.get("reading_level", {})
        if reading_level and reading_level.get("recommendations"):
            improved_data["reading_support"] = {
                "simplified_text": True,
                "sentence_frames": True,
                "visual_aids": True,
                "audio_support": True
            }
        
        # Apply UDL flag suggestions
        udl_flags = udl_data.get("udl_flags", [])
        for flag in udl_flags:
            if flag.get("suggestion"):
                flag_type = flag.get("type", "").lower()
                if flag_type == "representation":
                    improved_data["representation_support"] = {
                        "visual_aids": True,
                        "audio_alternatives": True,
                        "multiple_formats": True
                    }
                elif flag_type == "engagement":
                    improved_data["engagement_support"] = {
                        "choice_options": True,
                        "interest_connections": True,
                        "collaborative_options": True
                    }
                elif flag_type == "expression":
                    improved_data["expression_support"] = {
                        "multiple_assessment_formats": True,
                        "templates_provided": True,
                        "scaffolds_available": True
                    }
        
        return improved_data
    
    def add_visual_support(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add visual support to content"""
        enhanced_content = {**content}
        
        # Add visual elements based on content type
        if "objectives" in content:
            enhanced_content["visual_objectives"] = {
                "icon_set": "learning_objectives",
                "color_coding": True,
                "checklist_format": True
            }
        
        if "sequence" in content:
            enhanced_content["visual_sequence"] = {
                "timeline_format": True,
                "flowchart": True,
                "progress_indicator": True
            }
        
        if "activity" in content:
            enhanced_content["visual_activity"] = {
                "step_by_step_images": True,
                "materials_photos": True,
                "safety_diagrams": True
            }
        
        return enhanced_content
    
    def add_engagement_options(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add engagement options to content"""
        enhanced_content = {**content}
        
        enhanced_content["engagement_options"] = {
            "individual_work": True,
            "partner_work": True,
            "group_work": True,
            "choice_boards": True,
            "interest_based_activities": True
        }
        
        return enhanced_content
    
    def add_expression_choices(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add expression choices to content"""
        enhanced_content = {**content}
        
        enhanced_content["expression_choices"] = {
            "written_response": True,
            "oral_presentation": True,
            "visual_diagram": True,
            "digital_creation": True,
            "performance": True
        }
        
        return enhanced_content
    
    def create_udl_scaffolds(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Create UDL scaffolds for content"""
        enhanced_content = {**content}
        
        enhanced_content["udl_scaffolds"] = {
            "vocabulary_support": {
                "glossary": True,
                "word_wall": True,
                "context_clues": True
            },
            "reading_support": {
                "sentence_frames": True,
                "graphic_organizers": True,
                "audio_versions": True
            },
            "writing_support": {
                "templates": True,
                "sentence_starters": True,
                "peer_review": True
            },
            "math_support": {
                "manipulatives": True,
                "visual_models": True,
                "step_by_step": True
            }
        }
        
        return enhanced_content
    
    def validate_udl_improvement(self, original_data: Dict[str, Any], improved_data: Dict[str, Any]) -> bool:
        """Validate that UDL improvements have been applied"""
        original_score = self._extract_score(original_data.get("overall_score", "0%"))
        improved_score = self._extract_score(improved_data.get("overall_score", "0%"))
        
        # Check if score improved
        if improved_score > original_score:
            return True
        
        # Check if additional UDL support was added
        udl_support_added = any([
            "vocabulary_support" in improved_data,
            "reading_support" in improved_data,
            "representation_support" in improved_data,
            "engagement_support" in improved_data,
            "expression_support" in improved_data,
            "udl_scaffolds" in improved_data
        ])
        
        return udl_support_added

# Global handler instance
udl_handler = UDLLowCoverageHandler()
