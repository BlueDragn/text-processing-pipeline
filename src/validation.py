import re

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def validate_phone_number(phone_number):
    digits_only = re.sub(r"\D","", phone_number)
    if len(digits_only) >= 10:
        return True
    else:
        return False

def validate_experience_years(experience):
    digits = re.findall(r"\d+", experience)
    if digits:
        years = int(digits[0])
        if 0 <= years <= 50:
            return True
    return False

print(validate_email("test@example.com"))
print(validate_phone_number("123-456-7890"))
print(validate_experience_years("5 years of experience"))