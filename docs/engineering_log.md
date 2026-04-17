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