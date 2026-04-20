#!/usr/bin/env python3
"""
JSON STANDARDIZER: Converts all task groups to standard schema.

This script reads all task group JSON files, maps their various field names
to the standard unified schema, and saves the standardized versions.
"""

import json
from pathlib import Path
from typing import Dict, Any, List


def standardize_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a single task to standard schema."""
    
    standard_task = {
        # Always required
        "task_id": task.get("task_id"),
        "category": task.get("category"),
        "question": task.get("question"),
        "answer_type": task.get("answer_type"),
        "points": task.get("points"),
    }
    
    # Add optional common fields if present
    if "difficulty" in task:
        standard_task["difficulty"] = task["difficulty"]
    
    if "context" in task:
        standard_task["context"] = task["context"]
    
    if "dataset" in task:
        standard_task["dataset"] = task["dataset"]
    
    if "datasets" in task:
        standard_task["datasets"] = task["datasets"]
    
    if "document" in task:
        standard_task["document"] = task["document"]
    
    if "minimal_prompt" in task:
        standard_task["minimal_prompt"] = task["minimal_prompt"]
    
    if "tolerance" in task:
        standard_task["tolerance"] = task["tolerance"]
    
    if "target_dialect" in task:
        standard_task["target_dialect"] = task["target_dialect"]
    
    if "constraints" in task:
        standard_task["constraints"] = task["constraints"]
    
    # Build evaluation_criteria from various old field names
    evaluation_criteria = {
        "required_elements": [],
        "forbidden_elements": [],
        "syntax_check": False,
        "logic_check": False,
        "performance_check": False,
        "feature_check": False
    }
    
    # Map required_syntax -> required_elements
    if "required_syntax" in task:
        evaluation_criteria["required_elements"].extend(task["required_syntax"])
    
    # Map specific_features -> required_elements
    if "specific_features" in task:
        evaluation_criteria["required_elements"].extend(task["specific_features"])
    
    # Map requirements -> required_elements (flatten list of requirements)
    if "requirements" in task:
        evaluation_criteria["required_elements"].extend(task["requirements"])
    
    # Map expected_extraction -> required_elements
    if "expected_extraction" in task:
        evaluation_criteria["required_elements"].extend(task["expected_extraction"])
    
    # Map expected_structure -> required_elements
    if "expected_structure" in task:
        evaluation_criteria["required_elements"].append(task["expected_structure"])
    
    # Map sub_tasks -> required_elements
    if "sub_tasks" in task:
        evaluation_criteria["required_elements"].extend(task["sub_tasks"])
    
    # Map forbidden_syntax -> forbidden_elements
    if "forbidden_syntax" in task:
        evaluation_criteria["forbidden_elements"].extend(task["forbidden_syntax"])
    
    # Map forbidden_dialects -> forbidden_elements
    if "forbidden_dialects" in task:
        evaluation_criteria["forbidden_elements"].extend(task["forbidden_dialects"])
    
    # Map forbidden_features -> forbidden_elements
    if "forbidden_features" in task:
        evaluation_criteria["forbidden_elements"].extend(task["forbidden_features"])
    
    # Map common_mistakes -> forbidden_elements
    if "common_mistakes" in task:
        evaluation_criteria["forbidden_elements"].extend(task["common_mistakes"])
    
    # Handle existing evaluation field
    if "evaluation" in task:
        eval_obj = task["evaluation"]
        if isinstance(eval_obj, dict):
            if eval_obj.get("syntax_check"):
                evaluation_criteria["syntax_check"] = True
            if eval_obj.get("logic_check"):
                evaluation_criteria["logic_check"] = True
            if eval_obj.get("performance"):
                evaluation_criteria["performance_check"] = True
    
    # Add evaluation_criteria if it has any content
    if evaluation_criteria["required_elements"] or \
       evaluation_criteria["forbidden_elements"] or \
       any([evaluation_criteria["syntax_check"], 
            evaluation_criteria["logic_check"],
            evaluation_criteria["performance_check"]]):
        standard_task["evaluation_criteria"] = evaluation_criteria
    
    # Handle correct_answer - consolidate expected_answer and correct_answer
    # Preference: use correct_answer if both exist, else expected_answer
    if "correct_answer" in task:
        standard_task["correct_answer"] = task["correct_answer"]
    elif "expected_answer" in task:
        standard_task["correct_answer"] = task["expected_answer"]
    
    return standard_task


def standardize_task_group(input_file: Path) -> List[Dict[str, Any]]:
    """Standardize all tasks in a single task group file."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        tasks = json.load(f)
    
    standardized = []
    for task in tasks:
        standardized.append(standardize_task(task))
    
    return standardized


def main():
    """Convert all task group files to standard schema."""
    
    tasks_dir = Path("ford_data_analyst_benchmark/tasks")
    backup_dir = Path("ford_data_analyst_benchmark/tasks_backup")
    
    # Create backup directory
    backup_dir.mkdir(exist_ok=True)
    
    converted_count = 0
    error_count = 0
    
    print("=" * 100)
    print("STANDARDIZING TASK GROUPS")
    print("=" * 100)
    
    for task_file in sorted(tasks_dir.glob("task_group*.json")):
        try:
            print(f"\nProcessing: {task_file.name}...", end=" ")
            
            # Create backup
            backup_file = backup_dir / task_file.name
            with open(task_file) as f:
                backup_file.write_text(f.read())
            
            # Standardize
            standardized_tasks = standardize_task_group(task_file)
            
            # Write back with nice formatting
            with open(task_file, 'w', encoding='utf-8') as f:
                json.dump(standardized_tasks, f, indent=2, ensure_ascii=False)
            
            print(f"OK ({len(standardized_tasks)} tasks)")
            converted_count += 1
            
        except Exception as e:
            print(f"ERROR: {str(e)}")
            error_count += 1
    
    print("\n" + "=" * 100)
    print(f"CONVERSION COMPLETE")
    print("=" * 100)
    print(f"Successfully converted: {converted_count}")
    print(f"Errors: {error_count}")
    print(f"Backups saved to: {backup_dir}")
    print("\nAll task groups now use standard schema!")


if __name__ == "__main__":
    main()
