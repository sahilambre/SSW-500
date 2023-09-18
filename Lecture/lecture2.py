import random

# smaller = int (input ("Enter the smaller number: "))
# larger = int (input ("Enter the larger number: "))
# myNumber = random.randint (smaller, larger)
# count = 0
# while True:
#     count += 1
#     userNumber = int (input ("Enter your guess: "))
#     if userNumber < myNumber:
#         print ("Too small!")
#     elif userNumber > myNumber:
#         print ("Too large!")
#     else:
#         print ("Congratulations! You've got it in", count,"tries!")
#         break


data = "Hi there!"
for index in range (len (data)) :
    print (index, data[index])

name = "myfile.tx2"

print(name[-3:])

f = open ("integers.txt", 'w')
for count in range (5):
   number = random.randint (1, 5)
   f.write (str (number) + "\n")

f.close ()

f = open ("integers.txt", 'r')
text = f.read ()
print(text)

# for line in f:
#     print(line)

# 'First line.\nSecond line.\n'
# print (text)

f = open ("Test.txt", 'r')
while True:
    line = f.readline ()
    if line =="":
       break
    print (line)

# f = open ("integers.txt", 'r')
# sum = 0
# for line in f:
#     line = line.strip ()
#     number = int (line)
#     sum += number
# print ("The sum is", sum)
