# Created automatically by Cursor AI (2024-08-26)
"""
Runbook: Time Budget Overrun
Handles scenarios where lesson sections exceed allocated time
"""

from typing import Dict, List, Any, Tuple
from app.agents.sequence_planner import allocate_time, validate_time_budget

class TimeBudgetOverrunHandler:
    """Handles time budget overrun scenarios"""
    
    def __init__(self):
        self.max_overrun_threshold = 0.15  # 15% overrun threshold
        self.rebalance_strategies = [
            "reduce_duration",
            "split_lesson",
            "optimize_transitions",
            "combine_sections"
        ]
    
    def detect_overrun(self, sections: List[Dict[str, Any]], total_time: int) -> Dict[str, Any]:
        """Detect and analyze time budget overrun"""
        is_valid, message = validate_time_budget(sections, total_time)
        
        if is_valid:
            return {
                "overrun_detected": False,
                "message": "Time budget is within acceptable limits",
                "recommendations": []
            }
        
        allocated_time = sum(section.get("duration", 0) for section in sections)
        overrun_amount = allocated_time - total_time
        overrun_percentage = (overrun_amount / total_time) * 100
        
        return {
            "overrun_detected": True,
            "overrun_amount": overrun_amount,
            "overrun_percentage": overrun_percentage,
            "allocated_time": allocated_time,
            "total_time": total_time,
            "severity": self._determine_severity(overrun_percentage),
            "recommendations": self._generate_recommendations(overrun_percentage, sections)
        }
    
    def _determine_severity(self, overrun_percentage: float) -> str:
        """Determine severity of overrun"""
        if overrun_percentage <= 10:
            return "low"
        elif overrun_percentage <= 25:
            return "medium"
        else:
            return "high"
    
    def _generate_recommendations(self, overrun_percentage: float, sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate recommendations based on overrun severity"""
        recommendations = []
        
        if overrun_percentage <= 10:
            # Low overrun - optimize existing sections
            recommendations.extend([
                {
                    "strategy": "reduce_duration",
                    "description": "Reduce duration of non-critical sections",
                    "priority": "medium",
                    "estimated_savings": "5-10 minutes"
                },
                {
                    "strategy": "optimize_transitions",
                    "description": "Streamline transitions between sections",
                    "priority": "low",
                    "estimated_savings": "2-5 minutes"
                }
            ])
        
        elif overrun_percentage <= 25:
            # Medium overrun - consider splitting lesson
            recommendations.extend([
                {
                    "strategy": "split_lesson",
                    "description": "Split lesson into two days",
                    "priority": "high",
                    "estimated_savings": "Full overrun amount",
                    "implementation": "Create day 1 and day 2 versions"
                },
                {
                    "strategy": "reduce_duration",
                    "description": "Significantly reduce non-essential sections",
                    "priority": "medium",
                    "estimated_savings": "10-15 minutes"
                },
                {
                    "strategy": "combine_sections",
                    "description": "Combine related sections to reduce overhead",
                    "priority": "medium",
                    "estimated_savings": "5-10 minutes"
                }
            ])
        
        else:
            # High overrun - major restructuring needed
            recommendations.extend([
                {
                    "strategy": "split_lesson",
                    "description": "Split into multiple lessons",
                    "priority": "critical",
                    "estimated_savings": "Full overrun amount",
                    "implementation": "Create 2-3 separate lessons"
                },
                {
                    "strategy": "reduce_duration",
                    "description": "Dramatically reduce all non-essential content",
                    "priority": "high",
                    "estimated_savings": "15-20 minutes"
                },
                {
                    "strategy": "combine_sections",
                    "description": "Merge multiple sections into streamlined format",
                    "priority": "high",
                    "estimated_savings": "10-15 minutes"
                }
            ])
        
        return recommendations
    
    def auto_rebalance(self, sections: List[Dict[str, Any]], total_time: int) -> List[Dict[str, Any]]:
        """Automatically rebalance sections to fit time budget"""
        # Sort sections by priority (high priority first)
        priority_order = {"high": 3, "medium": 2, "low": 1}
        sorted_sections = sorted(
            sections, 
            key=lambda x: priority_order.get(x.get("priority", "medium"), 2),
            reverse=True
        )
        
        # Calculate total weight for proportional allocation
        total_weight = sum(priority_order.get(section.get("priority", "medium"), 2) for section in sorted_sections)
        
        # Allocate time proportionally, ensuring we don't exceed total_time
        remaining_time = total_time
        rebalanced_sections = []
        
        for i, section in enumerate(sorted_sections):
            weight = priority_order.get(section.get("priority", "medium"), 2)
            
            if i == len(sorted_sections) - 1:
                # Last section gets remaining time
                allocated_duration = remaining_time
            else:
                # Proportional allocation
                allocated_duration = max(1, int((weight / total_weight) * total_time * 0.9))  # 90% to leave buffer
                remaining_time -= allocated_duration
            
            rebalanced_section = {
                **section,
                "duration": allocated_duration,
                "original_duration": section.get("duration", 0),
                "adjustment": allocated_duration - section.get("duration", 0)
            }
            rebalanced_sections.append(rebalanced_section)
        
        return rebalanced_sections
    
    def suggest_split_lesson(self, sections: List[Dict[str, Any]], total_time: int) -> Dict[str, Any]:
        """Suggest how to split a lesson into multiple days"""
        # Group sections by logical flow
        day1_sections = []
        day2_sections = []
        
        # Simple heuristic: first half goes to day 1, second half to day 2
        midpoint = len(sections) // 2
        
        for i, section in enumerate(sections):
            if i < midpoint:
                day1_sections.append(section)
            else:
                day2_sections.append(section)
        
        # Calculate time for each day
        day1_time = sum(section.get("duration", 0) for section in day1_sections)
        day2_time = sum(section.get("duration", 0) for section in day2_sections)
        
        return {
            "split_recommended": True,
            "day1": {
                "sections": day1_sections,
                "total_time": day1_time,
                "focus": "Introduction and core concepts"
            },
            "day2": {
                "sections": day2_sections,
                "total_time": day2_time,
                "focus": "Application and assessment"
            },
            "transition_notes": "Day 2 should begin with a brief review of day 1 concepts"
        }
    
    def optimize_transitions(self, sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimize transitions to save time"""
        optimized_sections = []
        
        for i, section in enumerate(sections):
            optimized_section = {**section}
            
            # Optimize transition text
            if "transition" in section:
                original_transition = section["transition"]
                optimized_transition = self._optimize_transition_text(original_transition)
                optimized_section["transition"] = optimized_transition
                optimized_section["transition_savings"] = len(original_transition) - len(optimized_transition)
            
            optimized_sections.append(optimized_section)
        
        return optimized_sections
    
    def _optimize_transition_text(self, transition: str) -> str:
        """Optimize transition text for brevity"""
        # Simple optimization: remove unnecessary words
        optimizations = {
            "Now let's move on to": "Next:",
            "Let's transition to": "Next:",
            "Moving forward to": "Next:",
            "We will now proceed to": "Next:",
            "Let's continue with": "Next:"
        }
        
        optimized = transition
        for phrase, replacement in optimizations.items():
            if phrase.lower() in optimized.lower():
                optimized = optimized.replace(phrase, replacement)
                break
        
        return optimized
    
    def combine_sections(self, sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Combine related sections to reduce overhead"""
        if len(sections) < 3:
            return sections  # Need at least 3 sections to combine
        
        combined_sections = []
        i = 0
        
        while i < len(sections):
            if i + 1 < len(sections):
                # Check if sections can be combined
                current = sections[i]
                next_section = sections[i + 1]
                
                if self._can_combine_sections(current, next_section):
                    combined = self._combine_two_sections(current, next_section)
                    combined_sections.append(combined)
                    i += 2  # Skip next section
                else:
                    combined_sections.append(current)
                    i += 1
            else:
                combined_sections.append(sections[i])
                i += 1
        
        return combined_sections
    
    def _can_combine_sections(self, section1: Dict[str, Any], section2: Dict[str, Any]) -> bool:
        """Determine if two sections can be combined"""
        # Combine if both are low priority or if they're related
        priority1 = section1.get("priority", "medium")
        priority2 = section2.get("priority", "medium")
        
        if priority1 == "low" and priority2 == "low":
            return True
        
        # Combine if titles are related
        title1 = section1.get("title", "").lower()
        title2 = section2.get("title", "").lower()
        
        related_keywords = ["intro", "introduction", "warm", "review", "wrap", "close"]
        if any(keyword in title1 for keyword in related_keywords) and any(keyword in title2 for keyword in related_keywords):
            return True
        
        return False
    
    def _combine_two_sections(self, section1: Dict[str, Any], section2: Dict[str, Any]) -> Dict[str, Any]:
        """Combine two sections into one"""
        combined_duration = section1.get("duration", 0) + section2.get("duration", 0)
        
        return {
            "title": f"{section1.get('title', '')} & {section2.get('title', '')}",
            "description": f"{section1.get('description', '')} {section2.get('description', '')}",
            "duration": combined_duration,
            "priority": "medium",  # Combined sections become medium priority
            "materials": section1.get("materials", []) + section2.get("materials", []),
            "formative_check": f"{section1.get('formative_check', '')} {section2.get('formative_check', '')}",
            "transition": section2.get("transition", ""),
            "combined_from": [section1.get("title", ""), section2.get("title", "")]
        }

# Global handler instance
time_budget_handler = TimeBudgetOverrunHandler()
