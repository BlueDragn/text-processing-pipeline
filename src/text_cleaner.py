import re

def clean_text(text):
    if text is None:
        return None

    #1. Convert to lowercase
    text = text.lower()

    #2 Pattern: keep a-z, 0-9, space, @, ., and +
    pattern = re.compile(r"[^a-z0-9 @.+]")

    # replace unwanted characters with space
    text = pattern.sub(" ", text)
    #3. normalize whitespace
    text = " ".join(text.split())

    return text

if __name__ == "__main__":
    sample_text = "John doe !!! Email:john.doe@example.com has 3+ years of experience in Python programming. Contact: +1-234-567-8901"

    cleaned_text = clean_text(sample_text)
    print(cleaned_text)