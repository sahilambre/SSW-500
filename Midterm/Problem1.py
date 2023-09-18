
#! incorrect
# for n in range(1, 10):
#     print(n)


#* Correct
n = 1
while n <= 10:
    print(n)
    n += 1

#!incorrect
# n = 1
# while n < 10:
#     n = n + 1
#     print(n)

#* correct
for n in range(0, 10):
    print(n + 1)

#* correct 
n = 1
while n != 11:
    print(n)
    print(n + 1)
    n = n + 2