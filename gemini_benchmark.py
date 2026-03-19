import os
import json
import re
import datetime
import csv as csv_module
import subprocess
import time
from pathlib import Path
from gemini_client import create_client

def extract_final_answer(response_text):
    """
    Extract the final answer from response text using smart heuristics.
    
    Strategies (in order):
    1. Look for **Answer:** or **Final Answer:** marker AFTER any code blocks
    2. Check if extracted text is pandas metadata - if so, try to parse pandas output
    3. Look for **Answer:** at the start of a line (could be before code)
    4. If response contains code blocks and answer marker points to code, extract the code
    5. Fall back to extracting model ranking from pandas output
    6. Fall back to last non-empty line
    
    Args:
        response_text: The full response text
        
    Returns:
        The extracted final answer as a string
    """
    text = response_text.strip()
    
    # Strategy 1: Find ALL **Answer:** occurrences and use the LAST one
    # This handles cases where code is in between multiple answer markers
    answer_pattern = r'\*\*(?:Final\s+)?Answer:\*\*\s*(.+?)(?:\n\n(?=\*\*)|$)'
    matches = list(re.finditer(answer_pattern, text, re.DOTALL | re.IGNORECASE))
    if matches:
        # Try each match from last to first, looking for valid content
        for match in reversed(matches):
            extracted = match.group(1).strip()
            
            # Skip if it's just pandas metadata
            if extracted.startswith('```') and 'dtype' in extracted and 'Name:' in extracted:
                # This looks like pandas output metadata, try to extract model names from it
                models = _extract_models_from_pandas(extracted)
                if models:
                    return models
                continue
            
            # Clean up if it starts with code block marker
            if extracted.startswith('```'):
                # Extract code from this block
                code_pattern = r'```(?:\w+)?\n(.*?)\n```'
                code_match = re.search(code_pattern, extracted, re.DOTALL)
                if code_match:
                    code = code_match.group(1).strip()
                    if code:
                        return code
            elif extracted and len(extracted) > 0:
                # For explanation questions, check if this ends abruptly (likely cut off)
                # If it ends with ":" it's probably incomplete
                if extracted.rstrip().endswith(':'):
                    # This looks incomplete, try to get more content
                    # Look for the answer marker and grab everything after it more generously
                    full_answer_match = re.search(r'\*\*(?:Final\s+)?Answer:\*\*\s*(.+?)(?=\n(?:\*\*|$))', text, re.DOTALL | re.IGNORECASE)
                    if full_answer_match:
                        full_extracted = full_answer_match.group(1).strip()
                        if len(full_extracted) > len(extracted):
                            return full_extracted
                
                return extracted
    
    # Strategy 2: Try to extract ranking from pandas output in code blocks
    models = _extract_models_from_pandas(text)
    if models:
        return models
    
    # Strategy 3: Look for Answer: pattern without markdown
    answer_pattern2 = r'(?:^|\n)(?:Final\s+)?Answer:\s*(.+?)(?=\n\n|\n\*\*|$)'
    match2 = re.search(answer_pattern2, text, re.DOTALL | re.IGNORECASE)
    if match2:
        extracted = match2.group(1).strip()
        if extracted and len(extracted) > 0 and not extracted.startswith('```'):
            return extracted
    
    # Strategy 4: If response has code blocks, extract ONLY if substantial and no Answer marker found
    code_pattern = r'```(?:\w+)?\n(.*?)\n```'
    code_match = re.search(code_pattern, text, re.DOTALL)
    if code_match and not matches:  # Only if we didn't find Answer markers
        code = code_match.group(1).strip()
        if code and len(code) > 50:  # Substantial code only
            return code
    
    # Strategy 5: Fall back to last non-empty line
    lines = text.split('\n')
    for line in reversed(lines):
        stripped = line.strip().replace('**', '').replace('_', '').replace('`', '').strip()
        if stripped and not stripped.startswith('```') and len(stripped) > 2:
            return stripped
    
    return ''


def _extract_models_from_pandas(text):
    """
    Extract model names from pandas series/dataframe output.
    
    Looks for patterns like:
    model
    Fiesta      2419406
    Focus       2188894
    etc.
    
    Returns comma-separated list of model names in order, or empty string if not found.
    """
    # Look for lines with model names followed by numbers
    # Common Ford models: Fiesta, Focus, F150, Mustang, Bronco, Escape, Explorer, Fusion, Ranger, EdgeSUV
    ford_models = ['Fiesta', 'Focus', 'F150', 'Mustang', 'Bronco', 'Escape', 'Explorer', 'Fusion', 'Ranger', 'EdgeSUV']
    
    # Find all model mentions with numbers in the text
    found_models = []
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Skip metadata lines and headers
        if not line or 'dtype' in line or 'Name:' in line or line == 'model':
            continue
        
        # Check if line starts with a Ford model followed by whitespace and numbers
        for model in ford_models:
            if line.startswith(model) and any(c.isdigit() for c in line):
                if model not in found_models:
                    found_models.append(model)
                break
    
    if found_models:
        return ', '.join(found_models)
    
    return ''

def add_answer_formatting_instructions(question):
    """
    Append clear instructions for answer formatting to the question.
    This helps the AI provide structured answers that can be reliably extracted.
    
    Args:
        question: The original question text
        
    Returns:
        The question with appended formatting instructions
    """
    formatting_instructions = """

---
IMPORTANT - ANSWER FORMAT INSTRUCTIONS:
Please provide your response with the final answer clearly marked.

For simple answers (numbers, single words, names):
**Answer:** [your direct answer]

For code snippets (SQL, Python, etc.):
**Answer:**
```[language]
[your code]
```

For explanations with a clear conclusion:
**Answer:** [summary of your conclusion]

This format helps ensure your answer is correctly evaluated.
---"""
    return question + formatting_instructions

def scan_gemini_apis():
    """Discover available Gemini models using the client from v1."""
    def get_api_key():
        # Try environment variable
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            return api_key
        # Try gemini_test.py
        testfile = Path("gemini_test.py")
        if testfile.exists():
            text = testfile.read_text(encoding="utf-8")
            m = re.search(r"API_KEY\s*=\s*[\"'](.+?)[\"']", text)
            if m:
                return m.group(1)
        # Prompt user
        api_key = input("Enter Gemini API key: ").strip()
        return api_key
    print("[Progress] Discovering Gemini APIs...")
    try:
        api_key = get_api_key()
        print("[Progress] Gemini API key acquired.")
        client = create_client(api_key)
        models = client.models.list()
        print(f"[Progress] Found {len(models)} Gemini models.")
        return [m.name for m in models]
    except Exception as e:
        print(f"Error discovering Gemini models: {e}")
        return []

def scan_ford_tasks(tasks_dir):
    """Scan tasks directory for JSON files with questions."""
    print("[Progress] Scanning Ford task groups...")
    task_files = list(Path(tasks_dir).glob("*.json"))
    # Sort by numeric task_group extracted from filename
    def extract_level(tf):
        m = re.match(r"task_group(\d+)_", tf.name)
        return int(m.group(1)) if m else 999
    task_files.sort(key=extract_level)
    groups = []
    for tf in task_files:
        base = tf.stem
        base = re.sub(r'^task_group\d+_', '', base)
        group_name = ' '.join(word.capitalize() for word in base.split('_'))
        groups.append((tf.name, group_name))
    print(f"[Progress] Found {len(groups)} task groups.")
    return groups

def prompt_user_choice(options, prompt_text):
    print(prompt_text)
    for idx, opt in enumerate(options, 1):
        print(f"{idx}) {opt}")
    print("\nEnter the number(s) separated by commas, ranges (e.g., 1-10), or 'all':")
    choice = input().strip().lower()
    if choice == "all":
        return list(range(len(options)))
    selected = []
    for part in choice.split(","):
        part = part.strip()
        try:
            # Check if it's a range (e.g., "1-10")
            if "-" in part:
                start, end = part.split("-")
                start_idx = int(start.strip()) - 1
                end_idx = int(end.strip()) - 1
                # Add all indices in the range (inclusive)
                for i in range(start_idx, end_idx + 1):
                    if 0 <= i < len(options) and i not in selected:
                        selected.append(i)
            else:
                # Single number
                idx = int(part) - 1
                if 0 <= idx < len(options) and idx not in selected:
                    selected.append(idx)
        except Exception:
            continue
    return selected

def main():
    # Scan Gemini APIs
    print("[Progress] Starting Gemini benchmark script...")
    apis = scan_gemini_apis()
    print("[Progress] API discovery complete.")
    api_indices = prompt_user_choice(apis, "Here are a list of APIs available in the Gemini API, choose which one to process:")
    selected_apis = [apis[i] for i in api_indices]
    print(f"[Progress] Selected APIs: {selected_apis}\n")

    # Scan Ford tasks
    tasks_dir = "ford_data_analyst_benchmark/tasks"
    task_groups = scan_ford_tasks(tasks_dir)
    print("[Progress] Task group scan complete.")
    task_indices = prompt_user_choice([group[1] for group in task_groups], "Here are the Ford benchmark task groups, choose which to process:")
    selected_groups = [task_groups[i][0] for i in task_indices]
    print(f"[Progress] Selected task groups: {selected_groups}\n")

    # Prepare Gemini client
    print("[Progress] Setting up Gemini client...")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        testfile = Path("gemini_test.py")
        if testfile.exists():
            text = testfile.read_text(encoding="utf-8")
            m = re.search(r"API_KEY\s*=\s*[\"'](.+?)[\"']", text)
            if m:
                api_key = m.group(1)
    if not api_key:
        api_key = input("Enter Gemini API key: ").strip()
    client = create_client(api_key)
    print("[Progress] Gemini client ready.")

    # Begin processing
    print("[Progress] Beginning benchmark processing...")
    datasets_dir = "ford_data_analyst_benchmark/datasets"
    benchmarks_dir = "response_models"
    
    # Create response_models directory if it doesn't exist
    Path(benchmarks_dir).mkdir(parents=True, exist_ok=True)
    
    today = datetime.datetime.now().strftime("%Y%m%d")

    for api in selected_apis:
        print(f"\n[Progress] Processing API: {api}")
        results = []
        total_questions = 0
        api_stats = {
            "total_time": 0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "response_times": [],
            "question_count": 0
        }
        
        # First pass: count total questions
        for task_file in selected_groups:
            try:
                with open(f"ford_data_analyst_benchmark/tasks/{task_file}", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        total_questions += sum(1 for item in data if isinstance(item, dict) and item.get("question"))
                    elif isinstance(data, dict) and data.get("question"):
                        total_questions += 1
            except Exception:
                pass
        
        print(f"[Progress] Total questions to process: {total_questions}")
        current_question = 0
        
        for task_file in selected_groups:
            print(f"\n[Progress] Processing task group: {task_file}")
            # Load all questions from the selected task file
            try:
                with open(f"ford_data_analyst_benchmark/tasks/{task_file}", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        questions = [item["question"] for item in data if isinstance(item, dict) and item.get("question")]
                    elif isinstance(data, dict) and data.get("question"):
                        questions = [data["question"]]
                    else:
                        questions = []
            except Exception:
                questions = []

            print(f"[Progress] Found {len(questions)} questions in {task_file}.")
            for idx, question in enumerate(questions, 1):
                current_question += 1
                print(f"[Progress] Processing question {idx}/{len(questions)} ({current_question}/{total_questions} total)...")
                # Get dataset name and document name from task
                dataset_name = None
                document_name = None
                try:
                    with open(f"ford_data_analyst_benchmark/tasks/{task_file}", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for item in data:
                                if item.get("question") == question:
                                    dataset_name = item.get("dataset")
                                    document_name = item.get("document")
                                    break
                        elif isinstance(data, dict) and data.get("question") == question:
                            dataset_name = data.get("dataset")
                            document_name = data.get("document")
                except Exception:
                    pass

                # Load dataset preview if dataset is referenced
                dataset_preview = ""
                if dataset_name:
                    dataset_path = Path(datasets_dir) / dataset_name
                    if dataset_path.exists():
                        try:
                            with open(dataset_path, "r", encoding="utf-8") as f:
                                reader = csv_module.reader(f)
                                rows = list(reader)
                            header = rows[0] if rows else []
                            preview_rows = rows[1:] if len(rows) > 1 else []
                            csv_block = "\n".join([", ".join(row) for row in preview_rows])
                            dataset_preview = f"Dataset '{dataset_name}'\nColumns: {', '.join(header)}\nPreview:\n{csv_block}\n"
                        except Exception:
                            dataset_preview = f"Dataset '{dataset_name}' could not be loaded."

                # Load document content if document is referenced
                document_content = ""
                if document_name:
                    document_path = Path("ford_data_analyst_benchmark/documents") / document_name
                    if document_path.exists():
                        try:
                            with open(document_path, "r", encoding="utf-8") as f:
                                doc_text = f.read()
                            document_content = f"Document '{document_name}':\n{doc_text}\n"
                        except Exception:
                            document_content = f"Document '{document_name}' could not be loaded."

                # Add formatting instructions to question
                question_with_instructions = add_answer_formatting_instructions(question)
                # Combine dataset, document, and question in prompt
                prompt_parts = []
                if dataset_preview:
                    prompt_parts.append(dataset_preview)
                if document_content:
                    prompt_parts.append(document_content)
                prompt_parts.append(question_with_instructions)
                full_prompt = "\n".join(prompt_parts)
                print(f"[Progress] Sending to {api}...")

                # Real Gemini API call with timing
                start_time = time.time()
                try:
                    resp = client.models.generate_content(model=api, contents=full_prompt)
                    response_time = time.time() - start_time
                    
                    text = getattr(resp, "text", None)
                    if text is None:
                        try:
                            text = json.dumps(resp, default=str)
                        except Exception:
                            text = str(resp)
                    
                    # Extract token information from response
                    usage_metadata = getattr(resp, "usage_metadata", None)
                    input_tokens = 0
                    output_tokens = 0
                    if usage_metadata:
                        input_tokens = getattr(usage_metadata, "prompt_token_count", 0)
                        output_tokens = getattr(usage_metadata, "candidates_token_count", 0)
                    
                    # Track statistics
                    api_stats["total_time"] += response_time
                    api_stats["total_input_tokens"] += input_tokens
                    api_stats["total_output_tokens"] += output_tokens
                    api_stats["response_times"].append(response_time)
                    api_stats["question_count"] += 1
                    
                except Exception as e:
                    response_time = time.time() - start_time
                    text = f"ERROR: {e}"
                    input_tokens = 0
                    output_tokens = 0
                    api_stats["response_times"].append(response_time)
                    api_stats["question_count"] += 1

                # Extract final answer using smart heuristics
                final_answer = extract_final_answer(text)
                
                answer = {
                    "api": api,
                    "task_file": task_file,
                    "question": question,
                    "final_answer": final_answer,
                    # Save prompt and response as arrays of lines for multiline JSON readability
                    "prompt": full_prompt.split("\n"),
                    "response": text.split("\n"),
                    "performance": {
                        "response_time_seconds": round(response_time, 3),
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                        "total_tokens": input_tokens + output_tokens
                    }
                }
                results.append(answer)
                
                # Save JSON file after each question for real-time progress
                api_name = api.replace("models/", "").replace("/", "_")
                filename = f"{benchmarks_dir}/{api_name}_{today}_task_groups.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=2)
                
                avg_time = response_time if api_stats["question_count"] == 1 else api_stats["total_time"] / api_stats["question_count"]
                print(f"✓ Question {current_question}/{total_questions} completed (saved to JSON)")
                print(f"  └─ Time: {response_time:.2f}s | Tokens: {input_tokens + output_tokens} ({input_tokens} in, {output_tokens} out) | Avg: {avg_time:.2f}s")

        # Final save (already saved incrementally, but ensure final version is saved)
        api_name = api.replace("models/", "").replace("/", "_")
        filename = f"{benchmarks_dir}/{api_name}_{today}_task_groups.json"
        print(f"\n[Progress] All results saved to {filename}")
        
        # Print API performance summary
        if api_stats["question_count"] > 0:
            avg_time = api_stats["total_time"] / api_stats["question_count"]
            min_time = min(api_stats["response_times"]) if api_stats["response_times"] else 0
            max_time = max(api_stats["response_times"]) if api_stats["response_times"] else 0
            
            print(f"\n[Performance] {api} Summary:")
            print(f"  ├─ Total Time: {api_stats['total_time']:.2f}s")
            print(f"  ├─ Avg Time/Question: {avg_time:.2f}s")
            print(f"  ├─ Min/Max Time: {min_time:.2f}s / {max_time:.2f}s")
            print(f"  ├─ Total Tokens: {api_stats['total_input_tokens'] + api_stats['total_output_tokens']:,}")
            print(f"  ├─ Input Tokens: {api_stats['total_input_tokens']:,}")
            print(f"  ├─ Output Tokens: {api_stats['total_output_tokens']:,}")
            print(f"  └─ Questions Processed: {api_stats['question_count']}")
    
    print("\n" + "="*100)
    print("BENCHMARK PROCESSING COMPLETED!")
    print("="*100)
    print(f"Total questions processed: {total_questions}")
    print(f"Results saved to: {benchmarks_dir}/")
    print(f"Results file: {filename}")
    print("="*100 + "\n")
    
    # Ask if user wants to run evaluation
    print("\n[Evaluation] Would you like to run evaluation on the results?")
    eval_choice = input("Enter 'yes' or 'no': ").strip().lower()
    
    if eval_choice in ["yes", "y"]:
        print("\n[Evaluation] Starting evaluation script...")
        try:
            result = subprocess.run(
                ["python", "evaluate_benchmark_results.py", filename],
                capture_output=False,
                text=True
            )
            if result.returncode == 0:
                print("\n[Evaluation] Evaluation completed successfully!")
            else:
                print("\n[Evaluation] Evaluation script encountered an error.")
        except Exception as e:
            print(f"\n[Evaluation] Error running evaluation: {e}")
    else:
        print("\n[Info] Evaluation skipped. You can run it later with:")
        print(f"       python evaluate_benchmark_results.py {filename}\n")


if __name__ == "__main__":
    main()
