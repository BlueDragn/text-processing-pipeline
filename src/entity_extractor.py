text = "john doe email john.doe@example.com has 3+ years of experience in python programming. contact +1 234 567 8901"

current_number = ""
for char in text:
    if char.isdigit():
        current_number += char

    elif char in " -" and current_number:
        current_number += char
    else:
        if current_number:
            current_number = current_number.replace(" ", "")
            if len(current_number) == 10:
                    print("Phone number found:", current_number)
            current_number = ""




print(current_number)




