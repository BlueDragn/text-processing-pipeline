# Text Processing Pipeline

## Project Overview

The Text Processing Pipeline is a modular rule-based NLP project that converts unstructured resume text into structured profile data.

The pipeline processes raw text through multiple stages including cleaning, tokenization, entity extraction, skill extraction, validation, and profile generation.

The goal of this project is to demonstrate how raw textual information can be transformed into machine-readable structured data using a clean and modular architecture.

---

## Objective

Convert raw resume text into structured profile information using a reusable text processing pipeline.

---

## Pipeline Architecture

```text
Raw Text
    ↓
Text Cleaner
    ↓
Tokenizer
    ↓
Entity Extraction
    ↓
Skill Extraction
    ↓
Validation
    ↓
Profile Builder
    ↓
Structured Output
```

---

## Project Structure

```text
text-processing-pipeline/
│
├── data/
│
├── docs/
│   ├── engineering_log.md
│   └── engineering_note.md
│
├── notebooks/
│
├── src/
│   ├── text_cleaner.py
│   ├── tokenizer.py
│   ├── entity_extractor.py
│   ├── skill_extractor.py
│   ├── validation.py
│   ├── structure.py
│   └── pipeline_runner.py
│
├── tests/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Modules

### 1. text_cleaner.py

Responsible for preprocessing raw text.

Features:

- Convert text to lowercase
- Remove unwanted characters
- Preserve useful symbols required for extraction
- Normalize whitespace

Example:

```python
cleaned_text = clean_text(raw_text)
```

---

### 2. tokenizer.py

Converts cleaned text into tokens.

Features:

- Whitespace tokenization
- Handles empty input
- Removes trailing punctuation from tokens

Example:

```python
tokens = tokenize_text(cleaned_text)
```

---

### 3. entity_extractor.py

Extracts structured entities using regular expressions and controlled vocabularies.

Extracted Entities:

- Email addresses
- Phone numbers
- Experience years
- Job roles

Example Output:

```python
{
    "email": ["john@example.com"],
    "phone_number": ["+1 234 567 8901"],
    "experience_years": ["3+ years"],
    "roles": ["backend developer"]
}
```

---

### 4. skill_extractor.py

Extracts technical skills from text using a predefined skills database.

Supported Categories:

- Programming Languages
- Databases
- Frameworks
- Data & AI Skills
- Tools
- Cloud Technologies

Example Output:

```python
[
    "python",
    "sql",
    "docker",
    "aws"
]
```

---

### 5. validation.py

Validates extracted entities before profile generation.

Validation Rules:

#### Email

Checks:

- Contains "@"
- Contains "."

#### Phone Number

Checks:

- Minimum digit length

#### Experience Years

Checks:

- Numeric value exists
- Experience range between 0 and 50 years

---

### 6. structure.py

Builds the final structured profile.

Example Output:

```python
{
    "email": "john@example.com",
    "phone_number": "+1 234 567 8901",
    "experience_years": "3+ years",
    "skills": ["python", "sql"],
    "roles": ["backend developer"]
}
```

---

### 7. pipeline_runner.py

Integrates all pipeline stages into a complete workflow.

Pipeline Execution:

```python
cleaned_text = clean_text(text)

tokens = tokenize_text(cleaned_text)

entities = extract_entities(cleaned_text, tokens)

skills = extract_skills(cleaned_text, tokens)

profile = build_profile(...)
```

---

## Example Input

```text
John Doe is a backend developer with 3+ years of experience in python and SQL.

Contact:
john.doe@example.com

Phone:
+1 234 567 8901
```

---

## Example Output

```python
{
    "email": "john.doe@example.com",
    "phone_number": "+1 234 567 8901",
    "experience_years": "3+ years",
    "skills": ["python", "sql"],
    "roles": ["backend developer"]
}
```

---

## Testing

The pipeline was tested using multiple scenarios.

### Test Case 1

Normal Resume Input

Result:

- Passed

---

### Test Case 2

Missing Email

Result:

- Passed

Observation:

- Profile builder correctly stored email as None.

---

### Test Case 3

Invalid Email

Result:

- Passed

Observation:

- Invalid email was rejected while other entities were processed successfully.

---

### Test Case 4

Multiple Skills and Multi-word Roles

Result:

- Passed

Observation:

- Extracted multiple skills successfully.
- Extracted role:
  - machine learning engineer

---

### Test Case 5

Noisy Text Input

Result:

- Passed

Observation:

- Pipeline remained functional despite excessive symbols and formatting noise.

---

## Issues Discovered During Testing

### Issue 1

Skill Extraction Failure

Problem:

```text
docker.
```

was not matched as:

```text
docker
```

Root Cause:

Trailing punctuation survived tokenization.

Fix:

```python
token.strip(".,!?")
```

Added token normalization.

---

### Issue 2

Experience Extraction Limitation

Problem:

Regex only supported single-digit experience values.

Failed Examples:

```text
10 years
12+ years
15 years
```

Fix:

Updated regex:

```python
r"\d+\+?\s+years?"
```

to support multi-digit experience values.

---

## Known Limitations

Current implementation is rule-based.

Limitations:

- No Named Entity Recognition (NER)
- No machine learning models
- Limited role vocabulary
- Limited skills database
- Exact matching required for skills
- English text only

---

## Future Improvements

Possible future enhancements:

- spaCy-based Named Entity Recognition
- Machine Learning skill extraction
- Configurable skills database
- Resume parsing from files
- JSON export support
- Improved phone number handling
- Expanded role detection

---

## Learning Outcomes

This project demonstrates:

- Regular Expressions
- String Processing
- Tokenization
- Rule-Based Information Extraction
- Data Validation
- Modular Software Design
- Pipeline Architecture
- End-to-End Testing
- Debugging and Root Cause Analysis

---

## Project Status

**Version 1 Complete**

All planned modules have been implemented, integrated, tested, and documented.

The project successfully converts raw resume text into structured profile information using a modular rule-based processing pipeline.


