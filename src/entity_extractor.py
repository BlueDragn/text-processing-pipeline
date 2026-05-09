import re

# Extract email
def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    return re.findall(pattern, text)

#Extract phone number
def extract_phone_number(text):
    pattern = r"(?:\+\d{1,3}\s)?\d+\s+\d+\s?\d+"
    return re.findall(pattern, text)

# extract_experience_years(text)
def extract_experience_years(text):
    pattern = r"\d\+?\s+years?"
    return re.findall(pattern, text)

# extract_roles(text)
roles_db = ["data scientist", "machine learning engineer", "software developer", "python programmer","backend developer"]
def extract_roles(text):
    text = text.lower()
    extracted_roles = []
    for role in roles_db:
        if role in text:
            extracted_roles.append(role)
    return extracted_roles



def extract_entities(text, tokens):
    return{
        "email": extract_email(text),
        "phone_number": extract_phone_number(text),
        "experience_years": extract_experience_years(text),
        "roles": extract_roles(text)
    }



