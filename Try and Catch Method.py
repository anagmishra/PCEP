try:
    x = int(input("Enter a number:"))
except ValueError:
    print("Invalid integer")

try:
    x = [1, 2, 3, 4, 5]
    print(len(x))
except AttributeError:
    print("Attribute does not exist")