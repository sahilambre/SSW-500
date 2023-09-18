#Problem 4

import pandas as pd
import numpy as np
# import math

grades = {}

num_of_students = int(input("How many students do you want to enter grades for? "))

for element in range(num_of_students):
    name = input(f"Enter the name of student {element+1}: ")
    grade = np.random.randint(1, 101)
    grades[name] = grade

df = pd.DataFrame.from_dict(grades, orient='index', columns=['Grades'])

print(grades)
print(df)