import pandas as pd

student_data = [['Alice', 20, 'A', 85],
                ['Bob', 22, 'B', 78],
                ['Charlie', 19, 'A', 92],
                ['David', 21, 'C', 65],
                ['Eva', 20, 'B', 74]]

Data =pd.DataFrame(student_data, columns=['Name','Age','Grades','Marks'])
print(Data)
print( "#" * 50)
print(Data.head(3))
print("#" * 50)
print(Data[['Name', 'Marks']])
print("#" * 50)
print(Data[Data['Grades']=='A'])
