#Q1
even = 0
odd = 0
x = 0
while(True):
    x = int(input("Enter a number (Enter 0 to terminate the program):"))
    if(x == 0):
        break
    elif(x%2 == 0):
        even+=1
    else:
        odd+=1

print(f"The number of even numbers are {even}")
print(f"The number of odd numbers are {odd}")

#Q2
w = input("Enter a word: \n")
print("The word (without vowels) is:")
for char in w:
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        continue
    print(char, end="")