#Homework
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if(x>y):
    subtract = x-y
    print(f"The difference is {subtract}")
elif(x<y):
    add = x+y
    print(f"The sum is {add}")
else:
    product = x*y
    print(f"The product is {product}")


year = int(input("Enter a year: "))
if(year%4==0):
    if(year%100!=0 or year%400==0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
else:
    print("The year is not a leap year")