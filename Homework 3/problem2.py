# problem 2


sum = 0
count = 0

print("Enter a series of numbers, one per line. Press Enter when finished.")

while True:  
    user_input = input() 
    if user_input == "":
        break
    sum += float(user_input)
    count += 1

if count > 0:
    average = sum / count
else:
    average = 0

print("sum of ",count, " numbers is ", sum)
print("average is  ", average)