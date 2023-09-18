
# TODO: example 1
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third Side: "))

if a == b == c:
    print("This is an equilateral triangle")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("This is a right triangle")
else:
    print("This is neither equilateral nor right triangle")

# TODO: example 2 

data = [1, -2, 5, 6, 0, 5, 0, 3 ]

new_list = []

for i in data:
    if(i != 0):
        new_list.append(i)
    
print(new_list)

# TODO: example 3

number = int(input("enter a number: "))

for i in range(1,11):
    print(number, "x", i, "=", number * i)

# TODO: example 4

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)


# TODO: example 5

lst = [1, 2, 3, 4, 5, 2, 45, 45, 567, 892, 1, 892]

duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicates in the list:", duplicates)

# TODO: example 6

file = open("median.txt", "r")
numbers = [int(line.strip()) for line in file]
print("numbers in median.txt", numbers)
numbers.sort()
print("Sorted numbers: ", numbers)
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2-1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

print("The median is:", median)
