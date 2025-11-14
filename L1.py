# x = "\"Anag\""
# print(x, end = "\r")
# print("Hello World")

import time
for i in range(10):
    print(f"Installing...{i}", end = "\r")
    time.sleep(0.5)

print(" Installed")

# Homework
x = 10
print(x)
print(type(x))
y = 10.5
print(y)
print(type(y))
z = True
print(z)
print(type(z))
a = "Hello"
print(a)
print(type(a))
b = [1, 2, 3, 4, 5]
print(b)
print(type(b))
c = ("watermelon", "firemelon", "airmelon", "earthmelon", "elemelons")
print(c)
print(type(c))
d = {
    "Name": "Anag",
    "Age": 16,
    "Grade": 11
}
print(d)
print(type(d))
e = {"Anag", 16, 11}
print(e)
print(type(e))