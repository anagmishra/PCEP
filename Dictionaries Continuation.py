fruits = {'Apple': 10, 'Orange': 5, 'Banana': 8, 'Grape': 15}

sort = dict(sorted(fruits.items()))
print(sort)
student = {'Name': 'Tara', 'RollNo': 130046, 'Mark': 458, 'Age': 16}

print("Before Rename:", student)
student['Mark10'] = student.pop('Mark')
student['RegNo'] = student.pop('RollNo')

print("After Rename: ", student)