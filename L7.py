d1 = {'Adam Smith':'A','Judy Paxton':'B+'}
d2 = {'Mary Louise':'A','Patrick White':'C'}
d3 = d1| d2
print(d3)

A = {'Tamil':92, 'English':56, 'Maths':88, 'Science':97}
B = {'Tamil':94, 'English':74, 'Maths':88, 'Science':99}

for key, value in A.items():
    if key in B and B[key] == value:
        print(f"Both dictionaries have the same ",key," which have the same", value)