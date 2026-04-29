import re


text = "john doe email john.doe@example.com has 3+ years of experience in python programming. contact +1 234 567 8901"


# extract_email(text)

# extract_experience_years(text)
# extract_roles(text)



def extract_phone_number(text):
    # Define a regex pattern for phone numbers
    pattern = re.compile(r"\d+\s+\d+\s+\d+\s+\d+")
    return pattern.findall(text)



print(extract_phone_number(text))


