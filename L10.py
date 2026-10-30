def add(x):
    if(x==0):
        return x
    else:
        return x + add(x-1)
    
print(add(10))
