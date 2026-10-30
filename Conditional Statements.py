#Q1
n = int(input("Enter a number! \n"))

if(n%2==0):
        print("The number is even")
else:
        print("The number is odd")


#Q2
d = int(input("Enter the destionation distance in miles: \n"))
a = int(input("Enter the age of the passenger: \n"))

if(d<1000):
        if(a<12):
                print("$200")
        elif(a>=12 and a<=64):
                print("$300")
        else:
                print("$250")
else:
        if(a<12):
                print("$400")
        elif(a>=12 and a<=64):
                print("$500")
        else:
                print("$450")

#Q3
c = input("Enter your condition: \n")
ag = int(input("Enter your age: \n"))
if ag<12:
        if c == "Critical":
                print("Highest Priority")
        elif c == "Serious":
                print("Medium Priority")
        elif c == "Stable":
                print("Lowest Priority")
        else:
                print("Error")
elif ag>=12 and ag<=64:
        if c == "Critical":
                print("Highest Priority")
        elif c == "Serious":
                print("Medium Priority")
        elif c == "Stable":
                print("Lowest Priority")
        else:
                print("Error")
else:
        if c == "Critical":
                print("Highest Priority")
        elif c == "Serious":
                print("Medium Priority")
        elif c == "Stable":
                print("Lowest Priority")
        else:
                print("Error")

i = int(input("Enter income:"))
o = int(input("Enter 1 if health insurance is paid: \n Enter 2 if charitable donations are made: \n Enter 3 if both have been done: \n Enter 4 if neither has been done \n"))
it = 0
if i <= 10000:
        it = 0
elif i>10000 and i<=50000:
        it = 0.1*i
elif i>50000:
        it = 0.2*i

if o == 1:
        it = 0.95*it
elif o == 2:
        it = 0.9*it
elif o == 3:
        it = 0.85*it

print(f"Income tax is {it}")


i = float(input("Enter income in thalers:"))
it = 0.0
if(i <= 85528.0):
        it = 0.18*i