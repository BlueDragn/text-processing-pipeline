## Date: April 17

### Session 01

Text cleaner Implementation

### Objective

Build a text cleaning module for preprocessing raw text

### Work done

- Implement regex-based cleaning using allowed character set
- Preserved emails, numbers, and phone structure
- Normalized spacing using split and join

### Observations

- Basic string methods were insufficient
- Regex enabled pattern-based filtering

### Next Step

 Implement tokenizer module

---
---

### Session 02

Tokenizer and  Skill  EXtraction module

### Objective

Convert cleaned text into tokens and extract skills using controlled vocabulary.

### Work done

- Implement tokenizer using whitespace splitting
- Handled edge cases(empty input, None)
- Built skills extraction using  
   1. token matching (single-word skills)  
   2. phrase matching (multi-word skills)
- Used set to remove duplicates
- Ensured consistent output as list

### Observation

- Tokenizer depends on properly cleaned text
- Skill extraction depends on predefined skills_db
- Matching fails if input is not normalized (case sensitivity)

### Next Step

Entity extraction (name, email, experience, role)


## **Date:** May 23

## Entity Extraction, Validation and Pipeline Integration

---

## Objective

Complete the end-to-end resume information extraction pipeline by implementing entity extraction, validation, profile structuring, and full pipeline orchestration.

---

## Work Done

### Entity Extraction

- Implemented regex-based email extraction
- Implemented phone number extraction with optional country code support
- Implemented experience extraction using year-pattern matching
- Implemented role extraction using controlled vocabulary lookup

### Entity Aggregation

- Built centralized `extract_entities()` function
- Structured extracted entities into dictionary-based schema

### Validation Layer

- Implemented validation functions for:
  - emails
  - phone numbers
  - experience values

- Normalized phone numbers before validation using regex substitution
- Applied numeric range validation for experience values
- Filtered validated entities using list comprehensions

### Profile Structure Generation

- Built `build_profile()` function for standardized profile creation
- Handled missing values safely using conditional expressions
- Converted single-value entity lists into scalar fields
- Preserved skills and roles as collection-based fields

### Pipeline Integration

- Integrated all modules inside `pipeline_runner.py`
- Connected:
  - text cleaner
  - tokenizer
  - entity extractor
  - skill extractor
  - validation layer
  - profile builder

- Implemented sequential data flow from raw text to final structured profile output

---

## Observations

- Pipeline stages rely heavily on consistent interfaces between modules
- Cleaner quality directly impacts tokenization and downstream extraction accuracy
- Validation acts as a trust-filtering layer between extraction and final output
- List comprehensions simplify filtering and transformation operations
- Structured schema improves interoperability and downstream usability
- Rule-based extraction performs reliably for controlled and predictable text patterns
- Modular pipeline design improves readability, maintainability, and debugging

---

## Next Step

Run multiple end-to-end pipeline tests using noisy, incomplete, and varied resume inputs before closing Version 1 of the project.

## Tests

### Test 1 : Normal Valid Resume
text =
  """  
John DOe is a backend developer with 3+ years of experience in python and SQL.
Contact: john.doe@example.com  
phone: +1 234 567 8901  
"""
#### Result :
System behaved as expected

### Test 2: Missing Email
**INPUT**  

Resume text without email information but containing:
- phone number
- experience
- python
- docker


#### Expected Result  


Pipeline should:
- return `None` for email
- continue extracting remaining entities and skills correctly

#### Actual Result

Email handling worked as expected and final profile stored:
`"email": None`

During testing, an unrelated issue was discovered in skill extraction:
`docker` was not extracted successfully.

#### Root Cause

Tokenizer preserved trailing punctuation, causing token to become:
`docker.`

Skill extractor uses exact token matching, so:
`"docker"` did not match `"docker."`

#### Fix Applied

Normalized tokens during tokenization by stripping trailing punctuation using:

```python
token.strip(".,!?")
```


### Test 3: Invalid Email and Missing Experience

**Input**  

text = """  
Bob is a python programmer.  
Email: bobgmail.com  
Phone: +1 111 222 3333  
"""

Input resume text containing:

- invalid email address
- valid phone number
- role information
- skill information
- no experience information

#### Expected Result

Pipeline should reject the invalid email, return no experience value, and continue processing remaining information.

#### Actual Result

Invalid email was ignored during extraction.
No experience value was extracted.
Phone number, role, and skill extraction completed successfully.

#### Observation

The pipeline handled multiple missing or invalid fields gracefully.
Failure of one entity type did not affect extraction of other entities.
Profile generation correctly represented unavailable values as None.

### Test 4: Multiple Skills

**Input**  
text = """  
Sarah is a machine learning engineer skilled in python, django, flask, pandas, numpy, docker and aws.
"""

Resume text containing multiple technical skills and the role "machine learning engineer".

#### Expected Result

Pipeline should extract listed skills and identify the multi-word role.

#### Actual Result

Multiple skills and the role were extracted successfully.
Missing email, phone number, and experience fields were handled correctly.

#### Observation

Phrase matching supports extraction of both multi-word skills and multi-word roles.
A skill phrase "machine learning engineer" contained within a role title was also extracted as a skill.
This behavior is acceptable for the current rule-based implementation.



### Test 5: Noisy Text

**Input**  
text = """  
@@@ JOHN DOE ### PYTHON!!! developer $$$  
EMAIL::: john@example.com  
"""

Resume text containing excessive punctuation, symbols, mixed casing, and irregular formatting.

#### Expected Result

Pipeline should remove noise while preserving meaningful information required for extraction.

#### Actual Result

Email, phone number, experience, and skill information were extracted successfully.
Validation and profile generation completed successfully.

#### Observation

The pipeline remained functional despite heavily formatted input.
Text normalization preserved critical entities such as email addresses and phone numbers.

An additional limitation was observed:
special character sequences such as "@@@" were preserved because the cleaner allows the "@" character to support email extraction.

This behavior is acceptable for the current rule-based implementation but highlights a limitation of character-level cleaning.
