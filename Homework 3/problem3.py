#problem 3




salary = float(input("Enter the starting salary: $"))
percent = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("Year   Salary")

for i in range(1, years + 1):
    print( i,"\t", end="")
    print(" %.2f" % salary)
    salary = salary * (1 + percent / 100)