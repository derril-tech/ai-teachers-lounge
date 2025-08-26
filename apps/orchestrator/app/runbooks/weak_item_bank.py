# Created automatically by Cursor AI (2024-08-26)
"""
Runbook: Weak Item Bank
Handles scenarios where quiz item bank is insufficient or low quality
"""

from typing import Dict, List, Any, Tuple

class WeakItemBankHandler:
    """Handles weak item bank scenarios"""
    
    def __init__(self):
        self.minimum_items_per_type = 3
        self.minimum_difficulty_levels = 3
        self.quality_thresholds = {
            "clarity": 0.8,
            "relevance": 0.9,
            "difficulty_distribution": 0.7,
            "content_coverage": 0.8
        }
        self.difficulty_levels = ["easy", "medium", "hard"]
        self.item_types = ["multiple_choice", "multi_select", "numeric", "short_answer"]
    
    def detect_item_bank_issues(self, item_bank: Dict[str, Any]) -> Dict[str, Any]:
        """Detect issues with the item bank"""
        issues = []
        recommendations = []
        
        # Check item count per type
        item_counts = item_bank.get("item_counts", {})
        for item_type in self.item_types:
            count = item_counts.get(item_type, 0)
            if count < self.minimum_items_per_type:
                issues.append({
                    "type": "insufficient_items",
                    "description": f"Insufficient {item_type} items ({count} < {self.minimum_items_per_type})",
                    "severity": "high" if count == 0 else "medium",
                    "item_type": item_type,
                    "current_count": count,
                    "required_count": self.minimum_items_per_type
                })
        
        # Check difficulty distribution
        difficulty_distribution = item_bank.get("difficulty_distribution", {})
        for level in self.difficulty_levels:
            level_count = difficulty_distribution.get(level, 0)
            if level_count == 0:
                issues.append({
                    "type": "missing_difficulty",
                    "description": f"No items at {level} difficulty level",
                    "severity": "medium",
                    "difficulty_level": level
                })
        
        # Check content coverage
        content_coverage = item_bank.get("content_coverage", {})
        if content_coverage:
            coverage_score = content_coverage.get("score", 0)
            if coverage_score < self.quality_thresholds["content_coverage"]:
                issues.append({
                    "type": "poor_content_coverage",
                    "description": f"Poor content coverage ({coverage_score:.1%} < {self.quality_thresholds['content_coverage']:.1%})",
                    "severity": "medium",
                    "current_score": coverage_score,
                    "target_score": self.quality_thresholds["content_coverage"]
                })
        
        # Check item quality
        quality_metrics = item_bank.get("quality_metrics", {})
        if quality_metrics:
            for metric, threshold in self.quality_thresholds.items():
                if metric in quality_metrics:
                    score = quality_metrics[metric]
                    if score < threshold:
                        issues.append({
                            "type": "poor_quality",
                            "description": f"Poor {metric} quality ({score:.1%} < {threshold:.1%})",
                            "severity": "medium",
                            "metric": metric,
                            "current_score": score,
                            "target_score": threshold
                        })
        
        # Check for duplicate items
        duplicate_items = item_bank.get("duplicate_items", [])
        if duplicate_items:
            issues.append({
                "type": "duplicates",
                "description": f"Found {len(duplicate_items)} duplicate items",
                "severity": "low",
                "duplicate_count": len(duplicate_items)
            })
        
        # Check for biased items
        biased_items = item_bank.get("biased_items", [])
        if biased_items:
            issues.append({
                "type": "bias",
                "description": f"Found {len(biased_items)} potentially biased items",
                "severity": "high",
                "biased_count": len(biased_items)
            })
        
        # Generate recommendations
        recommendations = self._generate_item_bank_recommendations(issues, item_bank)
        
        return {
            "item_bank_issues_detected": len(issues) > 0,
            "total_issues": len(issues),
            "issues": issues,
            "recommendations": recommendations,
            "priority_actions": self._get_priority_actions(issues)
        }
    
    def _generate_item_bank_recommendations(self, issues: List[Dict[str, Any]], item_bank: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recommendations for improving item bank"""
        recommendations = []
        
        for issue in issues:
            if issue["type"] == "insufficient_items":
                recommendations.append({
                    "strategy": "increase_generator_count",
                    "description": f"Increase {issue['item_type']} item generation",
                    "priority": "high" if issue["severity"] == "high" else "medium",
                    "implementation": f"Generate {issue['required_count'] - issue['current_count']} additional {issue['item_type']} items",
                    "target_count": issue["required_count"]
                })
            
            elif issue["type"] == "missing_difficulty":
                recommendations.append({
                    "strategy": "add_difficulty_items",
                    "description": f"Add items at {issue['difficulty_level']} difficulty",
                    "priority": "medium",
                    "implementation": f"Generate 3-5 {issue['difficulty_level']} difficulty items",
                    "difficulty_level": issue["difficulty_level"]
                })
            
            elif issue["type"] == "poor_content_coverage":
                recommendations.append({
                    "strategy": "expand_content_coverage",
                    "description": "Expand content coverage across topics",
                    "priority": "medium",
                    "implementation": [
                        "Identify missing content areas",
                        "Generate items for uncovered topics",
                        "Ensure balanced topic distribution"
                    ]
                })
            
            elif issue["type"] == "poor_quality":
                recommendations.append({
                    "strategy": "improve_item_quality",
                    "description": f"Improve {issue['metric']} quality",
                    "priority": "medium",
                    "implementation": self._get_quality_improvement_strategies(issue["metric"])
                })
            
            elif issue["type"] == "duplicates":
                recommendations.append({
                    "strategy": "remove_duplicates",
                    "description": "Remove duplicate items",
                    "priority": "low",
                    "implementation": [
                        "Identify and remove exact duplicates",
                        "Consolidate similar items",
                        "Maintain item bank uniqueness"
                    ]
                })
            
            elif issue["type"] == "bias":
                recommendations.append({
                    "strategy": "address_bias",
                    "description": "Address biased items",
                    "priority": "high",
                    "implementation": [
                        "Review and revise biased items",
                        "Ensure cultural sensitivity",
                        "Apply bias detection filters"
                    ]
                })
        
        return recommendations
    
    def _get_quality_improvement_strategies(self, metric: str) -> List[str]:
        """Get strategies for improving specific quality metrics"""
        strategies = {
            "clarity": [
                "Simplify language and sentence structure",
                "Remove ambiguous wording",
                "Use clear, direct questions",
                "Provide clear answer choices"
            ],
            "relevance": [
                "Ensure alignment with learning objectives",
                "Connect to real-world applications",
                "Use current, relevant examples",
                "Match grade-level expectations"
            ],
            "difficulty_distribution": [
                "Balance easy, medium, and hard items",
                "Use difficulty calibration",
                "Ensure appropriate cognitive levels",
                "Match target student population"
            ],
            "content_coverage": [
                "Cover all learning objectives",
                "Include various topic areas",
                "Ensure comprehensive assessment",
                "Balance different content types"
            ]
        }
        
        return strategies.get(metric, ["Review and improve item quality"])
    
    def _get_priority_actions(self, issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Get prioritized actions based on issue severity"""
        priority_actions = []
        
        # Sort issues by severity (critical > high > medium > low)
        severity_order = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        sorted_issues = sorted(issues, key=lambda x: severity_order.get(x["severity"], 0), reverse=True)
        
        for issue in sorted_issues[:5]:  # Top 5 priority actions
            priority_actions.append({
                "action": self._get_action_for_issue(issue),
                "priority": issue["severity"],
                "description": issue["description"],
                "estimated_effort": self._estimate_effort(issue)
            })
        
        return priority_actions
    
    def _get_action_for_issue(self, issue: Dict[str, Any]) -> str:
        """Get specific action for an issue"""
        action_map = {
            "insufficient_items": "Generate additional items",
            "missing_difficulty": "Add difficulty-specific items",
            "poor_content_coverage": "Expand content coverage",
            "poor_quality": "Improve item quality",
            "duplicates": "Remove duplicates",
            "bias": "Address bias issues"
        }
        
        return action_map.get(issue["type"], "Review and improve")
    
    def _estimate_effort(self, issue: Dict[str, Any]) -> str:
        """Estimate effort required for an issue"""
        if issue["type"] == "insufficient_items":
            count_needed = issue.get("required_count", 0) - issue.get("current_count", 0)
            if count_needed <= 3:
                return "Low (1-2 hours)"
            elif count_needed <= 10:
                return "Medium (2-4 hours)"
            else:
                return "High (4-8 hours)"
        elif issue["type"] == "bias":
            return "High (requires careful review)"
        elif issue["type"] == "poor_quality":
            return "Medium (2-4 hours)"
        else:
            return "Low (1-2 hours)"
    
    def increase_generator_count(self, item_type: str, target_count: int, current_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Increase the number of items for a specific type"""
        items_needed = target_count - len(current_items)
        
        if items_needed <= 0:
            return current_items
        
        # Generate additional items based on type
        new_items = []
        
        if item_type == "multiple_choice":
            new_items = self._generate_multiple_choice_items(items_needed)
        elif item_type == "multi_select":
            new_items = self._generate_multi_select_items(items_needed)
        elif item_type == "numeric":
            new_items = self._generate_numeric_items(items_needed)
        elif item_type == "short_answer":
            new_items = self._generate_short_answer_items(items_needed)
        
        return current_items + new_items
    
    def _generate_multiple_choice_items(self, count: int) -> List[Dict[str, Any]]:
        """Generate multiple choice items"""
        items = []
        for i in range(count):
            items.append({
                "id": f"mcq_{i+1}",
                "type": "multiple_choice",
                "question": f"Sample multiple choice question {i+1}",
                "options": [
                    {"id": "a", "text": "Option A", "correct": True},
                    {"id": "b", "text": "Option B", "correct": False},
                    {"id": "c", "text": "Option C", "correct": False},
                    {"id": "d", "text": "Option D", "correct": False}
                ],
                "difficulty": "medium",
                "explanation": f"Explanation for question {i+1}"
            })
        return items
    
    def _generate_multi_select_items(self, count: int) -> List[Dict[str, Any]]:
        """Generate multi-select items"""
        items = []
        for i in range(count):
            items.append({
                "id": f"ms_{i+1}",
                "type": "multi_select",
                "question": f"Sample multi-select question {i+1}",
                "options": [
                    {"id": "a", "text": "Option A", "correct": True},
                    {"id": "b", "text": "Option B", "correct": True},
                    {"id": "c", "text": "Option C", "correct": False},
                    {"id": "d", "text": "Option D", "correct": False}
                ],
                "difficulty": "medium",
                "explanation": f"Explanation for question {i+1}"
            })
        return items
    
    def _generate_numeric_items(self, count: int) -> List[Dict[str, Any]]:
        """Generate numeric items"""
        items = []
        for i in range(count):
            items.append({
                "id": f"num_{i+1}",
                "type": "numeric",
                "question": f"Sample numeric question {i+1}",
                "correct_answer": 42.0,
                "tolerance": 0.1,
                "units": "units",
                "difficulty": "medium",
                "explanation": f"Explanation for question {i+1}"
            })
        return items
    
    def _generate_short_answer_items(self, count: int) -> List[Dict[str, Any]]:
        """Generate short answer items"""
        items = []
        for i in range(count):
            items.append({
                "id": f"sa_{i+1}",
                "type": "short_answer",
                "question": f"Sample short answer question {i+1}",
                "correct_answers": ["Sample answer"],
                "keywords": ["sample", "answer"],
                "max_length": 100,
                "difficulty": "medium",
                "explanation": f"Explanation for question {i+1}"
            })
        return items
    
    def filter_by_difficulty_blueprint(self, items: List[Dict[str, Any]], blueprint: Dict[str, int]) -> List[Dict[str, Any]]:
        """Filter items based on difficulty blueprint"""
        filtered_items = []
        
        for difficulty, target_count in blueprint.items():
            difficulty_items = [item for item in items if item.get("difficulty") == difficulty]
            
            # Take up to target count
            filtered_items.extend(difficulty_items[:target_count])
        
        return filtered_items
    
    def validate_item_bank_improvement(self, original_bank: Dict[str, Any], improved_bank: Dict[str, Any]) -> bool:
        """Validate that item bank improvements have been applied"""
        original_issues = self.detect_item_bank_issues(original_bank)
        improved_issues = self.detect_item_bank_issues(improved_bank)
        
        # Check if number of issues decreased
        if len(improved_issues["issues"]) < len(original_issues["issues"]):
            return True
        
        # Check if item counts improved
        original_counts = original_bank.get("item_counts", {})
        improved_counts = improved_bank.get("item_counts", {})
        
        for item_type in self.item_types:
            original_count = original_counts.get(item_type, 0)
            improved_count = improved_counts.get(item_type, 0)
            
            if improved_count > original_count:
                return True
        
        # Check if quality metrics improved
        original_quality = original_bank.get("quality_metrics", {})
        improved_quality = improved_bank.get("quality_metrics", {})
        
        for metric, threshold in self.quality_thresholds.items():
            if metric in improved_quality and metric in original_quality:
                if improved_quality[metric] > original_quality[metric]:
                    return True
        
        return False

# Global handler instance
item_bank_handler = WeakItemBankHandler()
