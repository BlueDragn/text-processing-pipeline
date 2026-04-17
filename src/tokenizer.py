def tokenize_text(text):
    if text is None:
        return []

    # Split the text into tokens based on whitespace
    tokens = text.split()

    return tokens


print(tokenize_text(None))