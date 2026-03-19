# Ford Data Analyst Super Benchmark (FDASB) v3.7

Professional-grade AI evaluation framework with 235 tasks across 27 categories, including stress testing, cognitive skills, and advanced content generation. Includes Gemini API benchmarking tools for testing Google's LLMs against real-world Ford data analyst scenarios.

**Status**: Production Ready | **Tasks**: 235 | **Points**: 7,115 | **Categories**: 27 | **Task Groups**: 27

## Contents of This Workspace

```
📦 OM_e-commerce/AI/
├── 📄 README.md (this file)
├── 🐍 Python Scripts:
│   ├── gemini_benchmark.py (Main: Interactive Gemini benchmarking with performance metrics)
│   ├── gemini_client.py (Utility: Google Gemini client initialization)
│   ├── evaluate_benchmark_results.py (Evaluation: Scores Gemini responses using BenchmarkScorer)
│   ├── gemini_test.py (Testing: Quick API connection test)
│   ├── run_single_model_call.py (Testing: Single API call verification)
│   ├── ai_test_connection.py (Testing: API authentication test)
│   ├── bench_gui.py (GUI: Benchmark interface)
│   ├── compute_sales_winner*.py (Analysis: Sales data processing)
│   └── evaluate_model_sql_vs_csv.py (Testing: SQL vs CSV model comparison)
│
├── 📁 ford_data_analyst_benchmark/ (Core benchmark structure)
│   ├── tasks/ (27 task group files with 235 total questions)
│   ├── datasets/ (4 CSV files with Ford data)
│   ├── documents/ (5 specification documents for document reading tasks)
│   ├── answers/ (Scoring metadata and example responses)
│   ├── evaluation/ (scorer.py - the scoring engine)
│   └── README.md (FDASB detailed documentation)
│
├── 📁 response_models/ (Output directory: Benchmark results from Gemini runs)
│   └── *.json (Saved responses with performance metrics and scores)
│
├── 📁 benchmarks/ (Legacy: Partial benchmark results)
│   └── *.json (Historical evaluation data)
│
├── .venv/ (Python virtual environment)
├── requirements.txt (Python dependencies)
└── info.txt (Setup information)
```

## Quick Start

### Option 1: Test API Connection (Fastest)
```bash
# Test if your API key works
python gemini_test.py
```

### Option 2: Run Single Model Evaluation (2-5 minutes)
```bash
# Benchmark one Gemini model on a few task groups
python gemini_benchmark.py
# Then follow prompts:
# - Select API: 1 (or 1-5 for multiple)
# - Select task groups: 1-5 (for tasks 1-5)
# Results saved to response_models/*.json
```

### Option 3: Run Full Benchmark (30-60 minutes)
```bash
# Complete evaluation of Gemini models
python gemini_benchmark.py
# Select: 1-10 for APIs, 1-27 for all task groups
# Automatic evaluation runs after completion
```

### Option 4: Evaluate Existing Results
```bash
# Evaluate previously saved benchmark responses
python evaluate_benchmark_results.py
```

## Overview

The FDASB v3.7 tests AI systems across 27 difficulty levels with 235 tasks, organized in 7 tiers:
- **Tier 1 (Data Fundamentals)**: Data Understanding, Cleaning, EDA, Statistics, SQL, Business Insights
- **Tier 2 (Advanced Data Skills)**: Instruction Following, Dataform, SQL Dialects, Complex SQL, Prompt Efficiency, Document Reading
- **Tier 3 (Software Engineering)**: Website Dev, Pipeline Dev, Architecture, Debugging, Performance, Code Review, Library Management
- **Tier 4 (Professional Skills)**: Communication, Security, Testing & QA
- **Tier 5 (Stress Testing)**: Saturation & Complexity Limits, Long-Context Handling, Sustained Performance & Fatigue
- **Tier 6 (Cognitive Skills)**: Context Switching & Task Clarity
- **Tier 7 (Content Generation)**: Writing & Content Generation

**Total Possible Score**: 7,115 points across all tasks

---

## Benchmark Structure (27 Levels, 235 Tasks)

### Tier 1: Data Fundamentals (6 Categories, 26 Tasks, 425 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **1** | Data Understanding | 5 | 50 | CSV loading, schema interpretation, data types |
| **2** | Data Cleaning | 4 | 60 | Nulls, duplicates, validation, missing values |
| **3** | EDA | 5 | 75 | Summary stats, distributions, correlations |
| **4** | Statistics | 4 | 80 | Hypothesis testing, significance, correlation |
| **5** | SQL Queries | 4 | 80 | SELECT, JOINs, aggregation, filtering |
| **6** | Business Insights | 4 | 80 | KPIs, trends, recommendations, root cause |

### Tier 2: Advanced Data Skills (6 Categories, 30 Tasks, 805 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **7** | Instruction Following | 5 | 135 | Multi-step logic, ordering, constraints |
| **8** | Dataform Development | 5 | 145 | Production SQL, dependencies, optimization |
| **9** | SQL Dialects | 5 | 130 | BigQuery, MySQL, PostgreSQL validation |
| **10** | Complex SQL | 5 | 180 | CTEs, window functions, recursion |
| **11** | Prompt Efficiency | 5 | 95 | Minimal context, implicit understanding |
| **12** | Document Reading | 5 | 120 | Spec extraction, requirements analysis |

### Tier 3: Software Engineering (7 Categories, 35 Tasks, 830 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **13** | Website Development | 5 | 120 | HTML/CSS/JS, React, forms, UX |
| **14** | Pipeline Development | 5 | 120 | ETL, Airflow DAGs, scheduling |
| **15** | Architecture & Design | 4 | 100 | System design, scalability, patterns |
| **16** | Debugging | 5 | 120 | Error analysis, root cause analysis |
| **17** | Performance Optimization | 5 | 120 | Query tuning, indexing, bottlenecks |
| **18** | Code Review & Issues | 5 | 125 | Missing functions, validation, handling |
| **19** | Library Management | 5 | 125 | Version conflicts, alternatives, migrations |

### Tier 4: Professional Skills (3 Categories, 15 Tasks, 400 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **20** | Communication & Docs | 5 | 125 | Docstrings, API docs, READMEs, clarity |
| **21** | Security & Best Practices | 5 | 125 | SQL injection, auth, validation, encryption |
| **22** | Testing & QA | 5 | 150 | Unit tests, integration, coverage, CI/CD |

### Tier 5: Stress Testing (3 Categories, 25 Tasks, 945 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **23** | Saturation & Complexity | 5 | 240 | Progressive complexity escalation, breaking points |
| **24** | Long-Context Handling | 5 | 240 | 100+ constraints, large codebases, 1000+ records |
| **25** | Sustained Performance | 10 | 465 | 10-task marathon to measure fatigue degradation |

### Tier 6: Cognitive Skills (1 Category, 10 Tasks, 270 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **26** | Context Switching | 10 | 270 | Topic/domain switching, explicit vs implicit clarity |

### Tier 7: Content Generation (1 Category, 10 Tasks, 330 Points)

| Level | Category | Tasks | Points | Description |
|-------|----------|-------|--------|-------------|
| **27** | Writing & Generation | 10 | 330 | Exact word counts, tone adaptation, content synthesis, audience targeting |

---

## Benchmark Summary

```
Total: 235 tasks | 27 categories | 7,115 maximum points
- Easy (20 pts)      : 55 tasks
- Medium (25-30 pts) : 120 tasks  
- Hard (30-45 pts)   : 60 tasks
```

---

## Folder Structure

### Root Workspace Directory

```
📦 AI/
├── README.md                               # This file
├── requirements.txt                        # Python dependencies
├── info.txt                                # Setup information
│
├── 🐍 MAIN BENCHMARK SCRIPTS
├── gemini_benchmark.py                     # Interactive Gemini benchmarking with:
│   ├── Model discovery (lists all 45+ available Gemini APIs)
│   ├── Task group selection (supports ranges: 1-10, 1,5,10, all)
│   ├── Real-time JSON saves per question
│   ├── Performance tracking (response time, token counts)
│   ├── Per-API summary statistics
│   └── Auto-invoked evaluation script
│
├── gemini_client.py                        # Gemini client initialization utility
├── evaluate_benchmark_results.py           # Evaluation engine for saved responses
│
├── 🧪 TEST & UTILITY SCRIPTS
├── gemini_test.py                          # Quick API connection test
├── run_single_model_call.py                # Single API call verification
├── ai_test_connection.py                   # API authentication test
├── bench_gui.py                            # GUI benchmark interface
├── compute_sales_winner.py                 # Sales analysis script
├── compute_sales_winner_nopandas.py        # Sales analysis (no pandas)
├── evaluate_model_sql_vs_csv.py            # SQL vs CSV comparison
├── batch_evaluate_tasks.py                 # Batch task evaluation
├── test_task_loader.py                     # Task loading verification
│
├── 📁 ford_data_analyst_benchmark/        # Core benchmark package
│   ├── README.md                           # FDASB detailed documentation
│   ├── tasks/                              # 27 task group files (235 total questions)
│   │   ├── task_group1_basic.json          # Data Understanding (5 tasks)
│   │   ├── task_group2_cleaning.json       # Data Cleaning (4 tasks)
│   │   ├── task_group3_eda.json            # EDA (5 tasks)
│   │   ├── task_group4_statistics.json     # Statistics (4 tasks)
│   │   ├── task_group5_sql.json            # SQL Queries (4 tasks)
│   │   ├── task_group6_business.json       # Business Insights (4 tasks)
│   │   ├── task_group7_instruction_following.json
│   │   ├── task_group8_dataform.json
│   │   ├── task_group9_sql_dialect.json
│   │   ├── task_group10_complex_sql.json
│   │   ├── task_group11_prompt_efficiency.json
│   │   ├── task_group12_document_reading.json
│   │   ├── task_group13_website_dev.json
│   │   ├── task_group14_pipeline_dev.json
│   │   ├── task_group15_architecture.json
│   │   ├── task_group16_debugging.json
│   │   ├── task_group17_performance.json
│   │   ├── task_group18_code_review.json
│   │   ├── task_group19_library_management.json
│   │   ├── task_group20_communication.json
│   │   ├── task_group21_security.json
│   │   ├── task_group22_testing.json
│   │   ├── task_group23_saturation.json
│   │   ├── task_group24_long_context.json
│   │   ├── task_group25_sustained_performance.json
│   │   ├── task_group26_context_switching.json
│   │   └── task_group27_writing_generation.json
│   │
│   ├── datasets/                           # 4 Ford datasets
│   │   ├── sales_data.csv
│   │   ├── warranty_claims.csv
│   │   ├── dealer_claims.csv
│   │   └── vehicle_telemetry.csv
│   │
│   ├── documents/                          # 5 specification documents
│   │   ├── sample_spec.txt                 # F150 warranty policy
│   │   ├── business_requirements.txt       # Quality improvement initiative
│   │   ├── technical_spec.txt              # Database & SQL standards
│   │   ├── data_dictionary.txt             # Field definitions
│   │   └── complex_requirements.txt        # Advanced analytical questions
│   │
│   ├── answers/
│   │   ├── answer_key.json                 # Scoring metadata
│   │   └── example_responses.json          # 235 example answers
│   │
│   └── evaluation/
│       └── scorer.py                       # Scoring engine (400+ lines)
│
├── 📁 response_models/                     # OUTPUT: Saved benchmark results
│   ├── gemini-2.5-flash_20260316_task_groups.json
│   ├── gemini-2.0-flash-lite_*.json
│   └── ... (additional Gemini model results)
│
├── 📁 benchmarks/                          # Legacy: Partial evaluation data
│   ├── batch_evaluation_summary_*.json
│   ├── benchmark_partial_gemini_*.json
│   ├── response_BASIC_*.json
│   └── ... (historical benchmark results)
│
├── 📁 .venv/                               # Python virtual environment
└── 📁 __pycache__/                         # Compiled Python cache
```

---

## Key Features of Gemini Benchmarking Tools

### gemini_benchmark.py - Main Benchmarking Tool

**Interactive Selection**:
- ✅ Discovers and lists 45+ available Gemini models
- ✅ Discovers and lists 27 task groups
- ✅ Supports flexible range selection: `1-10`, `1,5,10`, `1-5,8,10-15`, `all`
- ✅ Works with both single selections and ranges for both models and tasks

**Real-Time Performance Tracking**:
- ✅ Measures response time per question (in seconds)
- ✅ Captures token usage: input_tokens, output_tokens, total_tokens
- ✅ Displays per-question progress: `✓ Question 15/46 completed`
- ✅ Shows timing and tokens for each response

**Real-Time JSON Updates**:
- ✅ Saves responses after each question (not batch at end)
- ✅ Prevents data loss if process interrupted
- ✅ Can resume or analyze partial runs
- ✅ Format: `{model_name}_{date}_{task_groups}.json`

**Per-API Performance Summary**:
```
[Performance] models/gemini-2.5-flash Summary:
  ├─ Total Time: 110.25s
  ├─ Avg Time/Question: 2.40s
  ├─ Min/Max Time: 1.58s / 3.22s
  ├─ Total Tokens: 11,250 (Input: 8,200 | Output: 3,050)
  └─ Questions Processed: 46
```

**Auto-Evaluation Integration**:
- ✅ After processing completes, automatically offers to run evaluation
- ✅ Invokes `evaluate_benchmark_results.py` with saved results
- ✅ Provides immediate scoring and analysis
- ✅ No manual steps needed

### evaluate_benchmark_results.py - Evaluation Engine

- Uses BenchmarkScorer class (from `ford_data_analyst_benchmark/evaluation/scorer.py`)
- Scores each response on: exact_match, reasoning_score, combined_score (50/50 weighted)
- Generates detailed evaluation report
- Filters results by model, task group, or specific date
- Default looks for all `response_models/*.json` files

### Key Improvements Over Previous Versions

| Feature | Before | Now |
|---------|--------|-----|
| **Task Naming** | level1, level2, ... | task_group1, task_group2, ... |
| **Range Selection** | Had to type 1,2,3,4,5,6,7,8,9,10 | Type 1-10 |
| **API Flexibility** | Single model only | Multiple models, ranges supported |
| **JSON Updates** | All saved at end (risky) | Real-time per-question saves |
| **Performance Tracking** | No timing data | Full: time, tokens, averages |
| **Evaluation** | Manual separate step | Auto-invoke after completion |
| **Import Issues** | Circular imports | Fixed with separate gemini_client.py |
| **API Library** | google.generativeai (deprecated) | google-genai (modern) |
| **Output Directory** | benchmarks/response_models/ | response_models/ (simplified) |
| **Progress Visibility** | No per-question feedback | Checkmarks, timing, token counts |

---

## Included Resources

**Local Datasets** (in `datasets/` folder - see Data Resources section above):
- **sales_data.csv**: 300 records, sales by model/region/year with revenue
- **warranty_claims.csv**: 1,128 records with realistic data quality issues
- **dealer_claims.csv**: 533 records, dealer-level claims with status tracking
- **vehicle_telemetry.csv**: 547 records, 100 vehicles with 5-7 sensor readings each

**Real Ford Production Data in BigQuery** (for Level 24 stress testing):
- **Project**: `prj-eucxipa-d`
- **Dataset**: `eucx_medallia`
- **Table**: `vehicle_data_save` (210 million rows)
- Global vehicle inventory with: VIN, make, brand, engine type, build date, warranty dates, product type
- Stress-test against real production-scale data
- See [BIGQUERY_INTEGRATION.md](BIGQUERY_INTEGRATION.md) for queries and setup

### Specification Documents (in `documents/` folder - see Data Resources section above)

- **sample_spec.txt**: F150 warranty policy, coverage amounts, exclusions, claim validation
- **business_requirements.txt**: Quality improvement initiative KPIs, targets, methodology
- **technical_spec.txt**: Database standards, SQL naming conventions, performance criteria
- **data_dictionary.txt**: Field definitions, valid ranges, business meanings
- **complex_requirements.txt**: 5 advanced analytical questions with data requirements

### Evaluation Features

✅ **Multi-dimensional Scoring**: Accuracy, Reasoning, Insight, Communication, Code Quality, Dialect Score, Instruction Following
✅ **Timing Metrics**: Per-task execution time, total time, average, fastest/slowest tracking
✅ **SQL Dialect Validation**: BigQuery, MySQL, PostgreSQL syntax and feature checking
✅ **Code Quality Analysis**: Readability, documentation, naming conventions, syntax
✅ **Instruction Following**: Task ordering, subtask completion, constraint handling verification
✅ **Document Comprehension**: Specification extraction and requirement interpretation
✅ **Architecture Evaluation**: System design, scalability, trade-off analysis
✅ **Security Review**: SQL injection, authentication, validation, encryption checks

### Saturation & Stress Testing

Three special categories test AI performance under extreme conditions:

**Level 23 - Saturation & Complexity Limits**: Progressive escalation from moderate to extreme complexity. Identifies the breaking point where AI quality degrades. Tests multi-constraint handling and production-readiness at scale.

**Level 24 - Long-Context Handling**: Real production-scale stress testing using Ford's 210M row vehicle database:
- **Local Tests**: 1,100+ record datasets for baseline long-context testing
- **Real Ford Data**: Queries against `prj-eucxipa-d.eucx_medallia.vehicle_data_save` (210 million vehicles)
- Measures coherence and accuracy on production-scale data
- Can't rely on loading all data into memory—must use efficient SQL/distributed approaches

**Level 25 - Sustained Performance (10-Task Marathon)**: Sequential same-domain tasks to measure fatigue degradation. Compare Task 1 vs Task 10 quality to quantify performance drift over extended sessions. Detects when AI starts making careless errors or missing constraints.

---

## How to Use This Workspace

### Setup (One-Time)

1. **Activate Virtual Environment**:
   ```bash
   # PowerShell
   .\.venv\Scripts\Activate.ps1
   
   # Bash/Unix
   source .venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   - Get Gemini API key from [Google AI Studio](https://aistudio.google.com)
   - Set environment variable or add to your script:
     ```python
     import os
     os.environ['GEMINI_API_KEY'] = 'your_key_here'
     ```

### Running Benchmarks with Gemini

#### Quick Test (1 minute)
```bash
python gemini_test.py
```
Tests: API connectivity, authentication, and basic model availability.

#### Single Model Evaluation (5-15 minutes)
```bash
python gemini_benchmark.py
```
Interactive prompts:
- **Select APIs**: Type `1` for gemini-2.5-flash, or `1-5` for first 5 models
- **Select Task Groups**: Type `1-10` to test task groups 1-10, or `all` for all 27

Features:
- ✅ Discover all 45+ available Gemini models
- ✅ Select from multiple models (with range support)
- ✅ Pick specific task groups (with range support)
- ✅ Real-time progress tracking per question
- ✅ Performance metrics: response time, token counts
- ✅ Per-API summary statistics
- ✅ Auto-save results to `response_models/*.json`
- ✅ Auto-run evaluation after completion

#### Full Benchmark (30-60 minutes)
```bash
python gemini_benchmark.py
# Select: 1-10 (or specific models)
# Select: all (or 1-27 for all task groups)
```

**Output Example**:
```
✓ Question 15/46 completed (saved to JSON)
  └─ Time: 2.34s | Tokens: 245 (180 in, 65 out) | Avg: 2.40s

[Performance] models/gemini-2.5-flash Summary:
  ├─ Total Time: 110.25s
  ├─ Avg Time/Question: 2.40s
  ├─ Min/Max Time: 1.58s / 3.22s
  ├─ Total Tokens: 11,250
  ├─ Input Tokens: 8,200
  ├─ Output Tokens: 3,050
  └─ Questions Processed: 46

BENCHMARK PROCESSING COMPLETED!
Running evaluation script...
```

### Evaluating Results

After benchmark completes, results are automatically evaluated:
```bash
# Or manually evaluate saved results
python evaluate_benchmark_results.py
```

**Output Metrics**:
- Overall score and percentage
- Per-task-group breakdown
- Scoring components: exact_match, reasoning_score, combined_score
- Performance summary

### Analyzing Results

Results are saved to `response_models/` with the format:
```
{model_name}_{date}_{task_groups}.json
```

Example: `gemini-2.5-flash_20260316_task_groups_1-10.json`

Each response includes:
- question_text
- gemini_response
- response_time_seconds
- input_tokens
- output_tokens
- total_tokens
- exact_match
- reasoning_score
- combined_score

---

## Understanding the Benchmark

### Task Groups (27 Total)

**Group 1-6: Data Fundamentals**
- Basic CSV loading, cleaning, EDA, statistics, SQL, business insights
- Foundation skills for any data analyst role

**Group 7-12: Advanced Data Skills**
- Multi-step instructions, production SQL, dialect variations, document reading
- Real-world data engineering scenarios

**Group 13-19: Software Engineering**
- Full-stack development, pipeline design, architecture, debugging, optimization
- Integration of data skills with software best practices

**Group 20-22: Professional Skills**
- Documentation, security, testing, QA
- Enterprise-grade software development

**Group 23-25: Stress Testing**
- Escalating complexity limits, long-context handling, fatigue testing
- Identifies where AI performance degrades under pressure

**Group 26: Cognitive Skills**
- Context switching, parallel reasoning, task clarity

**Group 27: Content Generation**
- Writing under constraints: word count, tone, audience, format

### Scoring System

Each task is scored on multiple dimensions (0-1 scale):
- **Accuracy**: Correctness of the answer (50%)
- **Reasoning**: Quality of explanation (30%)
- **Insight**: Depth of analysis (15%)
- **Communication**: Clarity and presentation (5%)
- Other dimensions for specific task types: code quality, dialect correctness, instruction adherence

**Score Interpretation**:
- 90-100%: Expert / Production-ready
- 80-89%: Advanced / Strong capabilities
- 70-79%: Proficient / Good skills
- 60-69%: Competent / Basic understanding
- 50-59%: Developing / Limited capabilities
- <50%: Struggling / Needs improvement

---

## Data Resources

### Datasets (in `ford_data_analyst_benchmark/datasets/`)

**sales_data.csv**: 300 records
- Columns: model, region, units_sold, year, revenue_usd
- Models: F150, Escape, Bronco, Mustang
- Regions: US, EU, Asia
- Years: 2020-2025

**warranty_claims.csv**: 1,128 records
- Columns: claim_id, model, mileage, repair_cost, failure_code, claim_date, dealer_id, region
- Data quality issues: 5% missing mileage, 3% negative costs (real-world scenario)
- Notable: Dealer D14 has 2-3× more claims than average

**dealer_claims.csv**: 533 records
- Columns: dealer_id, claims_per_month, region, first_time_fix_rate
- Aggregated by dealership for trend analysis
- Outliers: D14, D25, D38 with elevated volumes

**vehicle_telemetry.csv**: 547 records
- Columns: vehicle_id, timestamp, engine_temp, battery_temp, speed, error_codes
- 100 vehicles with 5-7 sensor readings each
- Temperature anomalies: ~10% exceed normal range (>110°C)

### Specification Documents (in `ford_data_analyst_benchmark/documents/`)

**sample_spec.txt**: F150 Warranty Policy
- Coverage amounts and durations
- Exclusions list (normal wear, misuse, environmental, modifications)
- Deductible and claim validation criteria
- Regional variations

**business_requirements.txt**: Quality Improvement Initiative
- Objective: Reduce warranty claims by 25% in 18 months
- KPIs, targets, success criteria
- Required data sources and analytical approach
- 5-month delivery timeline

**technical_spec.txt**: Database & SQL Standards
- Technology: BigQuery (primary), PostgreSQL (backup)
- Table design, partitioning, clustering strategy
- SQL naming conventions and code standards
- Performance requirements
- Query optimization techniques

**data_dictionary.txt**: Field Definitions
- Detailed column descriptions for each table
- Valid ranges and business rules
- Null policies
- Data quality expectations
- Examples: claim_id, repair_cost, failure_code, mileage, model

**complex_requirements.txt**: Advanced Analytics
- 5 key analytical questions the system must answer
- Associated data requirements for each question
- Predictive modeling requirements
- Real-time vs batch processing needs
- Data quality and timeliness expectations

---

## How to Run the Benchmark

### How to Use

Create `responses.json` with your AI model's answers:

```json
{
  "responses": [
    {
      "task_id": "BASIC_01",
      "answer": "F150",
      "time_seconds": 2.5
    },
    {
      "task_id": "BASIC_02",
      "answer": "328000 units",
      "time_seconds": 1.8
    }
  ]
}
```

Then run `python run_benchmark.py` and select option 3.

---

## Detailed Task Descriptions

### Tier 1: Data Fundamentals Tasks

#### Level 1 - Data Understanding (5 tasks, 50 pts)
Basic comprehension of structured datasets. Load CSVs, understand schemas, count records.
- Example: "Load sales_data.csv. How many records? What columns?"

#### Level 2 - Data Cleaning (4 tasks, 60 pts)
Identify and handle data quality issues like missing values and outliers.
- Example: "Find 2 data quality issues in warranty_claims.csv"

#### Level 3 - Exploratory Data Analysis (5 tasks, 75 pts)
Pattern detection, trend analysis, ranking, distribution analysis.
- Example: "Which dealer has unusually high warranty claims?"

#### Level 4 - Statistical Analysis (4 tasks, 80 pts)
Hypothesis testing, distribution analysis, correlation, statistical significance.
- Example: "Is D14's warranty volume statistically unusual?"

#### Level 5 - SQL Queries (4 tasks, 80 pts)
Database logic, JOINs, aggregation, filtering, GROUP BY.
- Example: "Write SQL for total sales by region"

#### Level 6 - Business Insights (4 tasks, 80 pts)
Strategic reasoning, decision-making, recommendations based on data.
- Example: "What should Ford do about the D14 anomaly?"

### Tier 2: Advanced Data Skills Tasks

#### Level 7 - Instruction Following (5 tasks, 135 pts)
Multi-step tasks, correct ordering, constraint handling.
- Example: "Filter to US → Calculate average → Show trend"

#### Level 8 - Dataform Development (5 tasks, 145 pts)
Production SQL with dependencies, optimization, best practices.
- Example: "Design Dataform models for warranty analysis pipeline"

#### Level 9 - SQL Dialects (5 tasks, 130 pts)
Dialect-specific syntax: BigQuery STRUCT/ARRAY, MySQL limitations, PostgreSQL JSON.
- Example: "Convert MySQL query to BigQuery syntax"

#### Level 10 - Complex SQL (5 tasks, 180 pts)
CTEs, window functions, recursion, partitioning.
- Example: "Write recursive CTE to find hierarchical relationships"

#### Level 11 - Prompt Efficiency (5 tasks, 95 pts)
Minimal context prompts, implicit understanding required.
- Example: "One-sentence instruction. Get it right without clarification."

#### Level 12 - Document Reading (5 tasks, 120 pts)
Extract requirements from specifications, understand constraints.
- Example: "From warranty spec: What's the deductible for F150?"

### Tier 3: Software Engineering Tasks

#### Level 13 - Website Development (5 tasks, 120 pts)
HTML/CSS/JavaScript, React, forms, responsiveness, UX.
- Example: "Build responsive dashboard form for data entry"

#### Level 14 - Pipeline Development (5 tasks, 120 pts)
ETL design, Airflow DAGs, scheduling, error handling.
- Example: "Design Airflow pipeline for daily warranty data processing"

#### Level 15 - Architecture & Design (4 tasks, 100 pts)
System design, scalability, performance, trade-offs.
- Example: "Design scalable data warehouse for Ford analytics"

#### Level 16 - Debugging (5 tasks, 120 pts)
Identify errors, root cause analysis, systematic troubleshooting.
- Example: "Fix broken SQL query and explain the error"

#### Level 17 - Performance Optimization (5 tasks, 120 pts)
Query tuning, indexing, bottleneck identification, scaling.
- Example: "Optimize slow query affecting reporting dashboard"

#### Level 18 - Code Review & Issue Detection (5 tasks, 125 pts)
Identify missing functions, validation, error handling, security issues.
- Example: "Find 5+ issues in this production code"

#### Level 19 - Library & Dependency Management (5 tasks, 125 pts)
Version conflicts, library selection, alternatives, migrations.
- Example: "Resolve conflicting dependencies: pandas vs polars"

### Tier 4: Professional Skills Tasks

#### Level 20 - Communication & Documentation (5 tasks, 125 pts)
Docstrings, API documentation, READMEs, clarity, examples.
- Example: "Write comprehensive API documentation with examples"

#### Level 21 - Security & Best Practices (5 tasks, 125 pts)
SQL injection prevention, authentication, validation, encryption.
- Example: "Find security vulnerabilities and fix them"

#### Level 22 - Testing & Quality Assurance (5 tasks, 150 pts)
Unit tests, integration tests, test strategies, coverage, CI/CD.
- Example: "Design comprehensive test suite with CI/CD integration"

### Tier 5: Stress Testing Tasks

#### Level 23 - Saturation & Complexity Limits (5 tasks, 240 pts)

Tests where AI breaks down as complexity increases. Progressive escalation to identify breaking points.

**Tasks:**
1. **Moderate Complexity**: Join 3 tables, clean data, calculate 5 metrics, identify outliers
2. **High Complexity**: Process 10+ CSV files with schema variations, normalize, create 8 metrics
3. **Very High**: Production-quality real-world messy data with modeling (50 pts)
4. **Multi-Dimensional**: 4 regions × 8 categories × 12 time periods with forecasting (50 pts)
5. **Ultimate**: End-to-end workflow with all 10 steps complete (55 pts)

**What it Tests:**
- Ability to handle increasingly complex requirements
- Whether quality degrades beyond certain complexity thresholds
- Handling of multiple simultaneous constraints
- Production-readiness at scale

---

#### Level 24 - Long-Context Handling (5 tasks, 240 pts)

Tests whether AI maintains accuracy and coherence with 100+ requirements and large codebases.

**Tasks:**
1. **Extract Requirements**: 50-line spec with 15 requirements and dependencies
2. **Large Codebase Analysis**: 100+ line codebase with architectural issues
3. **Large Dataset**: 1000+ records with pattern discovery and relationships
4. **Extended Workflow**: 20-step workflow tracking decisions and dependencies
5. **Multi-Document Integration**: Correlate across 5 specifications, resolve conflicts

**What it Tests:**
- Memory and context management capability
- Pattern recognition in large datasets
- Maintaining coherence across extended reasoning chains
- Ability to integrate information from multiple sources
- Finding subtle patterns in large amounts of data

---

#### Level 25 - Sustained Performance & Fatigue Testing (10 tasks, 465 pts)

**The 10-Task Marathon** - Measures performance degradation over extended sessions.

**Structure:**
- Tasks 1-3: Warm-up (basic SQL, Python, analysis)
- Tasks 4-5: Complexity increases, detect early fatigue
- Task 5: **MIDPOINT** - Comprehensive code review (critical quality check)
- Tasks 6-7: Post-midpoint, fatigue mounting
- Tasks 8-9: High difficulty despite fatigue (SQL security audit, ML pipeline)
- Task 10: **FINAL MARATHON TASK** - Integration test suite, compared to Task 1

**Scoring Note:** Compare Task 10 quality to Task 1 quality to quantify fatigue degradation.

**What it Tests:**
- Sustained quality over extended sequences
- Point at which performance degrades significantly
- Recovery capability between tasks
- "Attention deficit" - missing details after many tasks
- Consistency: early tasks vs late tasks

**Fatigue Indicators:**
- Later tasks show more errors or missing edge cases
- Reasoning becomes shorter/shallower over time
- Code quality (comments, error handling) decreases
- Mistakes increase (typos, logic errors)
- Task completion time changes significantly
- Careless errors appear (forgetting requirements, skipping steps)

---

#### Level 26 - Context Switching & Task Clarity (10 tasks, 270 pts)

Tests whether AI can switch between different topics/domains without getting confused or mixing up contexts.

**The Question:** When you switch from discussing Python to asking for SQL, does AI:
- A) Try to do SQL inside Python code (confusion)?
- B) Return just SQL as requested (clean switch)?
- C) Ask for clarification about the switch?

**Task Progression:**

1. **Basic Switch**: Writing Python → asking for SQL query (should get pure SQL)
2. **Domain Switch**: Data analysis context → API design (should get API design, not more analysis)
3. **Implicit Marking**: No explicit "SWITCH" or "NEW TOPIC" marker, just implicit switch (tests clarity with context hints)
4. **Rapid Switches**: Multiple quick topic changes (1-Python 2-HTML 3-SQL 4-API) without explicit markers (tests context management)
5. **Nested Switches**: Complex multi-level switches with integration (write Python → show SQL → integrate → error handling → architecture)
6. **Vague Switches**: "Now do the other thing" (tests AI ability to ask for clarification vs guessing)
7. **Conceptual Transfer**: Apply SQL optimization patterns to API caching (tests cross-domain reasoning)
8. **Parallel Contexts**: Maintain two contexts simultaneously (Python + SQL synchronized and traced)
9. **Conflicting Names**: Same variable name 'data' in Python and SQL (tests disambiguation and clarity)
10. **Recursive Workflow**: 6-stage multi-context chain with inheritance (tests context preservation across stages)

**What it Tests:**

| Aspect | Question |
|--------|----------|
| **Clean Switching** | Does it produce output for the new domain only, or mix contexts? |
| **Explicit vs Implicit** | Does it need "SWITCHING:" markers or understand implicit context changes? |
| **Clarity Seeking** | When vague, does it ask clarifying questions or guess? |
| **Parallel Contexts** | Can it keep two contexts (Python + SQL) synchronized? |
| **Context Inheritance** | Can it maintain context through a 6-stage workflow? |
| **Conflict Resolution** | How does it handle name collisions (same variable/table name)? |
| **Rapid Switching** | Quality degradation with fast topic changes? |

**Scoring Indicators:**

- **Clean Switch** (Good): SQL query returned, no Python code
- **Mixed Contexts** (Bad): SQL attempt wrapped in Python or vice versa
- **Asks Clarification** (Excellent): "Do you mean X?" when ambiguous
- **Guesses** (Okay): Makes reasonable assumption with caveat
- **Quality Loss** (Bad): Later switches show more errors or confusion
- **Full Context Preserved** (Excellent): All stages 1-6 correct with proper integration

---

#### Level 27 - Writing & Content Generation (10 tasks, 330 pts)

Tests AI's ability to generate original written content under specific constraints: exact word counts, tone adaptation, audience targeting, format conversion, and information synthesis.

**The Question:** Can AI write effectively under multiple simultaneous constraints, or does it struggle with competing requirements?

**Task Progression:**

1. **Exact Word Count**: Summarize a 520-word article in exactly 100 words (±5%) while retaining key points
2. **Note Synthesis**: Convert 10 scattered meeting notes into a polished 200-word product requirements document
3. **Tone Adaptation**: Same technical concept explained three ways - for CTO (technical), Product Manager (business value), and End User (simple language)
4. **Format Conversion**: Convert narrative specification into structured format with overview, acceptance criteria, technical requirements, edge cases
5. **Multi-Constraint**: Write 300-350 word API documentation with 3 code examples, covering all required topics
6. **Audience Adaptation**: Communicate same migration announcement to 3 audiences - executives, managers, and individual contributors (150 words each)
7. **Expansion Without Padding**: Expand 20-word concept into 300 words of technical depth without repetition or filler
8. **Brevity Challenge**: Compress 410-word email to exactly 200 words without losing key information
9. **Business Case**: Write persuasive 250-word business case for system implementation with quantified benefits
10. **Technical Blog Post**: Write 800-word technical article with 2-3 code examples, covering definition, advantages, disadvantages, real-world use case, next steps

**What it Tests:**

| Aspect | Question |
|--------|----------|
| **Word Count Accuracy** | Can it hit exact targets (±5%) consistently? |
| **Synthesis** | Can it extract clarity from chaos (unstructured notes)? |
| **Tone Shifting** | Can it adapt same content to different audiences/contexts? |
| **Format Flexibility** | Can it restructure information into different frameworks? |
| **Multi-Constraint Balance** | When requirements compete (word limit, coverage, tone), which wins? |
| **Expansion Skill** | Does expansion add value or just repeat/pad? |
| **Compression Skill** | Can it remove fluff while preserving essentials? |
| **Audience Awareness** | Does it genuinely adapt or superficially change wording? |
| **Quantification** | Can it translate vague concepts into concrete numbers? |
| **Depth Integration** | Can it explain technical topics accessibly with code examples? |

**Scoring Indicators:**

- **Word Count** (Strict): ±5% of target (miss = 0 points for this task)
- **Synthesis Quality** (Good): Extracts key points, removes redundancy, creates narrative
- **Tone Match** (Excellent): Different vocabulary/depth for each audience, not just find-replace
- **Structure Adherence** (Good): Follows requested format perfectly
- **Balance** (Excellent): Meets all constraints without sacrificing any one over others
- **Content Quality** (Good): No padding, no repetition, value-added expansion
- **Professional Finish** (Excellent): Reads naturally, not stilted or forced

---

## Scoring System

### Scoring Dimensions

Each task is evaluated on relevant dimensions (0-1 scale for each):

1. **Accuracy** (50% typical): Correctness of the answer
2. **Reasoning** (30% typical): Quality of explanation and logic
3. **Insight** (15% typical): Depth of analysis or innovation
4. **Communication** (5% typical): Clarity and presentation
5. **Code Quality** (varies): For coding tasks - readability, comments, structure
6. **Dialect Score** (varies): For SQL tasks - syntax correctness, best practices
7. **Instruction Following** (varies): For multi-step tasks - ordering, completeness
8. **Writing Quality** (varies): For content generation - clarity, tone, audience fit, constraint adherence

**Scoring Formula**: Each dimension is scored 0-1, weighted by importance, then multiplied by task points.

### Score Interpretation

| Score Range | Interpretation | AI Capability |
|-------------|-----------------|----------------|
| 90-100% | Expert | Production-ready, minimal review needed |
| 80-89% | Advanced | Strong capabilities with minor gaps |
| 70-79% | Proficient | Good skills but some gaps remain |
| 60-69% | Competent | Basic understanding, needs guidance |
| 50-59% | Developing | Limited capabilities, training needed |
| <50% | Struggling | Significant gaps, not suitable for production |

### Category Performance Analysis

Look for patterns to guide improvement:
- **Weak in Tier 1**: Address fundamentals before advanced skills
- **Weak in Tier 2**: Need advanced SQL and data modeling training
- **Weak in Tier 3**: Software engineering and architecture gaps
- **Weak in Tier 4**: Communication and testing rigor needed

---

## Task Format (JSON Schema)

Each task file contains an array of task objects:

```json
[
  {
    "task_id": "BASIC_01",
    "category": "Data Understanding",
    "difficulty": "easy|medium|hard",
    "question": "Your question text here",
    "answer_type": "text|code|list|number",
    "correct_answer": "Expected answer",
    "points": 50,
    
    "optional_fields": {
      "dataset": "sales_data.csv",
      "document": "sample_spec.txt",
      "target_dialect": "BigQuery",
      "sub_tasks": ["filter", "aggregate"],
      "correct_flow": "filter -> aggregate",
      "common_mistakes": ["missing filter", "wrong aggregate"]
    }
  }
]
```

---

## Dependencies

### Python Packages

```
google-genai          # Google's Gemini API client
google.generativeai   # Alternative (deprecated) Gemini library
pandas               # Data handling and analysis
numpy                # Numerical operations
```

### Installation

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install google-genai pandas numpy
```

### System Requirements

- **Python**: 3.8 or higher
- **Virtual Environment**: Recommended (.venv/ included)
- **API Key**: Google Gemini API key (free tier available)

---

## Advanced Features

### Timing Analysis

The benchmark tracks execution time for each task to identify:
- Overall efficiency (total time for all 180 tasks)
- Average time per task
- Which tasks take longest
- Time spent per category
- Performance trends across complexity levels

Timing metrics help identify:
- Slow reasoning or processing
- Areas requiring optimization
- Inconsistent performance

### SQL Dialect Validation

Automatically validates SQL syntax for:

**BigQuery**:
- STRUCT and ARRAY syntax
- SAFE functions
- Forbidden: ANY_VALUE with Dataform

**MySQL**:
- Version-specific features
- JSON operators
- Partition syntax

**PostgreSQL**:
- Recursive CTEs
- JSON operators
- Window function syntax

### Code Quality Metrics

Evaluated dimensions:
- Readability (clear variable names, proper structure)
- Documentation (comments, docstrings)
- Best practices (conventions, error handling)
- Syntax correctness (valid Python/SQL)

### Instruction Following Verification

For multi-step tasks, validates:
- Correct task ordering
- All required subtasks completed
- Common mistakes avoided
- Constraints respected

---

## Extending the Benchmark

### Add New Task Categories

1. Create new task file: `level23_yourCategory.json`
2. Add 5+ task objects following the JSON schema
3. Update `run_benchmark.py` to load the new file
4. Update `answers/answer_key.json` with new metadata

### Add New Datasets

1. Create CSV in `data/` folder
2. Reference in task JSON: `"dataset": "your_file.csv"`
3. Tasks can load and analyze this data

### Add New Specification Documents

1. Create text file in `documents/` folder
2. Reference in task: `"document": "your_spec.txt"`
3. Task tests requirement extraction and understanding

---

## Example: Testing Custom AI Model

### Step 1: Run Your Model

Have your AI model answer all 180 tasks. Record answers and timing.

### Step 2: Format Responses

Create `my_model_responses.json`:

```json
{
  "responses": [
    {
      "task_id": "BASIC_01",
      "answer": "F150",
      "time_seconds": 2.3
    },
    {
      "task_id": "BASIC_02",
      "answer": "328000",
      "time_seconds": 1.9
    },
    ...
  ]
}
```

### Step 3: Run Benchmark

```bash
python run_benchmark.py
# Select option 3: Load custom responses
# Enter: my_model_responses.json
```

### Step 4: Analyze Results

Review:
- Overall score and percentage
- Category breakdown (which areas strong/weak)
- Timing analysis
- Top 5 and bottom 5 tasks
- Score distribution

### Step 5: Iterate

- Compare multiple model versions
- Track improvement over time
- Focus on weak categories
- Measure impact of changes

---

## Technology Stack

- **Python 3.x**: Benchmark runner and scoring engine
- **Pandas**: Data loading and manipulation
- **NumPy**: Numerical operations
- **JSON**: Task definitions and responses
- **Difflib**: Text similarity for matching answers

---

## Version History

| Version | Changes | Status |
|---------|---------|--------|
| **v3.7** (Current) | Added Gemini benchmarking tools, interactive range selection, real-time JSON updates, performance metrics, evaluation integration. Fixed circular imports and API library. Task files renamed to task_groupN_ format. | Production Ready |
| **v3.0** | Added Code Review, Library Management, Communication, Security, Testing. Consolidated documentation. | Stable |
| **v2.0** | Added Instruction Following, Dataform, SQL Dialects, Complex SQL, Prompt Efficiency, Document Reading | Legacy |
| **v1.0** | Initial release with 6 basic categories | Legacy |

---

## Common Questions

### Q: What if my model doesn't have all task answers?

A: Leave out those task_ids from responses.json. The scorer will calculate percentage based on completed tasks.

### Q: How do I test a specific category?

A: Edit `run_benchmark.py` to load only certain level files, or copy specific file and run separately.

### Q: Can I modify tasks?

A: Yes, edit the JSON files directly. Scoring rules are in `evaluation/scorer.py`.

### Q: How are timing metrics used?

A: For analysis only. Faster isn't always better - quality matters too. Timing helps identify bottlenecks.

### Q: What if database access is needed?

A: All tasks use included CSV files. No external database required.

### Q: Can I add my own datasets?

A: Yes, add CSV files to `data/` folder and reference in task JSON with `"dataset": "your_file.csv"`.

---

## Support

For issues:
1. Verify Python 3.8+ installed
2. Check API key configured
3. Review task files in correct locations
4. Run `python gemini_test.py` to verify setup

---

## Troubleshooting & Common Issues

### API Key Issues

**Error: "API key not found"**
1. Set environment variable: `export GEMINI_API_KEY=your_key`
2. Or add to Python script:
   ```python
   import os
   os.environ['GEMINI_API_KEY'] = 'your_key_here'
   ```
3. Get free API key: https://aistudio.google.com

### Import Errors

**Error: "No module named google.genai"**
```bash
pip install google-genai
```

**Error: "Circular import gemini_benchmark"**
- Fixed in current version - uses separate `gemini_client.py`

### Task Loading Issues

**Error: "task_groupX_*.json not found"**
- Verify files are in `ford_data_analyst_benchmark/tasks/`
- Check naming: must be `task_groupN_category.json` (not levelN_)

**Error: "Document not found"**
- Verify document files in `ford_data_analyst_benchmark/documents/`
- Required: sample_spec.txt, business_requirements.txt, technical_spec.txt, data_dictionary.txt, complex_requirements.txt

### Performance Issues

**Slow responses**: Normal for Gemini API, especially with long contexts.
- Check internet connection
- Try single task group first (e.g., 1-5)
- Monitor token usage - longer responses = longer processing

**Out of memory**: With very large task groups (20+), consider:
- Process fewer task groups at once
- Results are auto-saved, so you can resume later

### File Not Found Errors

Ensure paths are correct:
```
workspace/
  ford_data_analyst_benchmark/
    tasks/          ← All task_groupN_*.json files
    datasets/       ← CSV files
    documents/      ← All 5 .txt specification files
    evaluation/
      scorer.py
```

---

## Next Steps

### 1. Test Your Setup
```bash
# Verify API connectivity
python gemini_test.py
```

### 2. Run a Quick Benchmark
```bash
python gemini_benchmark.py
# Select: 1 (first Gemini model)
# Select: 1-5 (first 5 task groups)
# Takes ~2-5 minutes
```

### 3. Analyze Results
Review `response_models/*.json` for:
- Response times
- Token usage
- Scores for each question
- Areas of strength and weakness

### 4. Run Full Benchmark
```bash
python gemini_benchmark.py
# Select: 1-10 (multiple models)
# Select: all (all 27 task groups)
# Takes ~30-60 minutes
```

### 5. Compare Models
Run benchmark on different Gemini versions:
- gemini-2.5-flash
- gemini-2.0-flash-lite
- gemini-1.5-pro
- etc.

Compare results to identify best model for your use case.

---

## Documentation References

- **[ford_data_analyst_benchmark/README.md](ford_data_analyst_benchmark/README.md)**: Detailed FDASB structure, scoring system, task descriptions
- **[ford_data_analyst_benchmark/documents/business_requirements.txt](ford_data_analyst_benchmark/documents/business_requirements.txt)**: Ford quality improvement initiative details
- **[ford_data_analyst_benchmark/documents/technical_spec.txt](ford_data_analyst_benchmark/documents/technical_spec.txt)**: Database and SQL standards
- **[ford_data_analyst_benchmark/documents/data_dictionary.txt](ford_data_analyst_benchmark/documents/data_dictionary.txt)**: Field definitions and data validation rules

---

## Support & Contact

For issues, improvements, or feature requests:
1. Check Troubleshooting section above
2. Review documentation in `ford_data_analyst_benchmark/README.md`
3. Examine log output from `gemini_benchmark.py`
4. Check response JSON files in `response_models/` for detailed error messages

---

**Last Updated**: March 16, 2026
**Status**: Production Ready
**Total Tasks**: 235 | **Total Points**: 7,115 | **Task Groups**: 27
2. Check dependencies: `pip install -r requirements.txt`
3. Ensure you're in the correct directory
4. Review example_responses.json for answer format
5. Check scorer.py for scoring logic

---

## License

Internal Ford Motor Company use only.

---

**Ready to benchmark your AI?** Run `python run_benchmark.py` now.

For detailed configuration, see `answers/answer_key.json` for scoring rubric and `evaluation/scorer.py` for implementation details.

