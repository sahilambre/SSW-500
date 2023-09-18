# Complexity analysis
# -------------------------------------
import time
problemSize = 10000000
print ("%12s%16s" % ("Problem Size", "Seconds"))
for count in range (5):
    start = time.time ()
    # The start of the algorithm
    work = 1
    for x in range (problemSize):
        work += 1
        work -= 1
        # The end of the algorithm
        elapsed = time.time () - start
    print ("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2

problemSize = 1000
print ("%12s%15s" % ("Problem Size", "Iterations"))
for count in range (2):
    number = 0
    # The start of the algorithm
    work = 1
    for j in range (problemSize):
        for k in range (problemSize):
            number += 1
            work += 1
            work -= 1
            # The end of the algorithm
    print("%12s%15s" % (problemSize, number))
    problemSize *= 2
# Returns the nth Fibonacci number using recursive function
def fib_1 (n):  
    if n == 1:
        return 0
    elif n <= 3 and n!=1:
        return 1
    else:
        return fib_1 (n-1) + fib_1 (n-2)

i = int (input("Enter the number of terms? "))
print ("The",i,"Fibonacci number is --->",fib_1(i))