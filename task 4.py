students =[
    {"name":"zeyad","grades":[80, 90, 95]},
   {"name":"omar","grades":[85, 95, 90]},
   {"name":"mohamed","grades":[90, 85, 80]}
   ]

def CalculateAverage(grades):
    return sum(grades) / len(grades)

for student in students:
    print(f"{student['name']} - Average Grade: {CalculateAverage(student["grades"])}")
    