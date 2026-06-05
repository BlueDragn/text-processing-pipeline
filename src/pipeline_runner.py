from text_cleaner import clean_text
from tokenizer import tokenize_text
from entity_extractor import extract_entities
from skill_extractor import extract_skills

from validation import (
    validate_email,
    validate_phone_number,
    validate_experience_years
)
from structure import build_profile

text = """
John Doe is a backend developer with 3+ years of experience in python and SQL.
Contact: john.doe@example.com
phone: +1 234 567 8901
"""

cleaned_text = clean_text(text)
print("Cleaned Text:", cleaned_text)

tokens = tokenize_text(cleaned_text)
print("Tokens:", tokens)

entities = extract_entities(cleaned_text, tokens)
print("Entities:", entities)

skills = extract_skills(cleaned_text, tokens)
print("Skills:", skills)

email = entities["email"]
phone = entities["phone_number"]
experience_years = entities["experience_years"]
roles = entities["roles"]

valid_email = [
    e for e in email if validate_email(e)
]
print("Valid Emails:", valid_email)
valid_phone = [
    p for p in phone if validate_phone_number(p)
]
print("Valid Phones:", valid_phone)

valid_experience = [
    exp for exp in experience_years if validate_experience_years(exp)
]
print("Valid Experience Years:", valid_experience)

profile = build_profile(
    valid_email,
    valid_phone,
    valid_experience,
    skills,
    roles
)

print(profile)