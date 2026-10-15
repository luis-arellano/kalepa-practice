# Insurance Submission Processor

## Background
You work at an insurtech company. Brokers submit commercial insurance applications via email, and the data arrives in inconsistent formats. Your job is to build a Python script that cleans, validates, and summarizes this data.

## Task
Write a Python script (`process_submissions.py`) that reads `data/submissions.json` and performs the following:

### 1. Data Cleaning
- Normalize `business_name`: trim whitespace
- Normalize `coverage_type`: title case (e.g., "general liability" → "General Liability")
- Normalize `state`: uppercase (e.g., "ca" → "CA")
- Normalize `broker_email`: lowercase
- Parse `annual_revenue` into a numeric value (remove `$`, commas, handle "N/A" → `None`)
- Parse `employee_count` into an integer
- Normalize `effective_date` and `expiration_date` to ISO format (`YYYY-MM-DD`)
- Parse each `prior_losses[].amount` into a numeric value

### 2. Validation
Flag submissions as **invalid** if any of the following are true:
- Missing `id`
- Missing or empty `business_name`
- Missing `broker_email`
- Missing `expiration_date`
- `annual_revenue` is missing or not parseable

### 3. Duplicate Detection
Identify potential duplicate submissions based on matching `business_name` (case-insensitive) AND `naics_code`.

### 4. Risk Summary
For each **valid, non-duplicate** submission, calculate:
- `total_prior_losses`: sum of all prior loss amounts
- `loss_years`: number of years with losses > $0
- `risk_flag`: "HIGH" if total losses > $100,000 or loss_years >= 2, otherwise "STANDARD"

### 5. Output
Write results to `output/summary.json` with the following structure:
```json
{
  "processed_at": "2026-10-14T...",
  "total_submissions": 6,
  "valid_submissions": 3,
  "invalid_submissions": [{"id": "...", "reasons": ["..."]}],
  "duplicates": [{"id": "...", "duplicate_of": "..."}],
  "risk_summary": [
    {
      "id": "...",
      "business_name": "...",
      "coverage_type": "...",
      "annual_revenue": 2500000,
      "total_prior_losses": 12000,
      "loss_years": 1,
      "risk_flag": "STANDARD"
    }
  ]
}
```

## Requirements
- Python 3.10+
- No external dependencies (stdlib only)
- Include at least basic tests in `test_process.py`

## How to Run
```bash
python process_submissions.py
python -m pytest test_process.py -v
```
