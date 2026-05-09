import re
a = "Hello!!!"
b = "Email: john@gmail.com"
c = "3+ years !!!"

a = re.sub("!", "", a)
b = re.sub(": ", " ", b)
b = b.lower()

pattern = "[+!]"
c = re.sub(pattern, "", c)


print(a)
print(b)
print(c)
