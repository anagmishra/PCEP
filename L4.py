n = int(input("Enter a number! \n"))

if(n%2==0):
        print("The number is even")
else:
        print("The number is odd")



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