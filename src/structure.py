def build_profile(
        email,
        phone_number,
        experience_years,
        skills,
        roles
):
    profile = {
        "email": email[0] if email else None,
        "phone_number": phone_number[0] if phone_number else None,
        "experience_years": experience_years[0] if experience_years else None,
        "skills": skills,
        "roles": roles
    }
    return profile

profile = build_profile(
    ["test@example.com"],
    ["+1 234 567 8901"],
    ["3+ years"],
    ["Python", "JavaScript"],
    ["Developer", "Engineer"]
)
