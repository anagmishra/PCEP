email = input("Enter your Email Address please:\n")
e = ""
for char in email:
    if char == "@":
        break
    e+=char

print(f"Your email address (before the @ symbol) is: ", e)