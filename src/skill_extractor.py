skills_db = [
    # programming languages
    "python",
    "java",
    "c++",
    "javascript",
    "ruby",
    "go",

    #Database
    "sql",
    "mysql",
    "mongodb",
    "postgresql",

    #Frameworks / Libraries
    "django",
    "flask",
    "react",
    "node.js",

    # Data / AI
    "machine learning",
    "deep learning",
    "data analysis",
    "data visualization",
    "pandas",
    "numpy",

    # Tools
    "git",
    "docker",
    "linux",

    # Cloud
    "aws",
    "azure",
    "gcp"

    ]

def extract_skills(cleaned_text,tokens):
    matched_skills = set()
    for skill in skills_db:
        if " " in skill:
            if skill in cleaned_text:
                matched_skills.add(skill)
        else:
            if skill in tokens:
                matched_skills.add(skill)
    return list(matched_skills)


print(extract_skills("john playing football and music", ["football","music"]))