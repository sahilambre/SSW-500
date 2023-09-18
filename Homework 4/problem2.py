
#* Write the Fibonacci sequence as a linear (non-recursive) algorithm. Let the function take in the 
#* desired term in the Fibonacci sequence, and return the appropriate number. For example, the 
#* sequence starts as 1, 1, 2, 3, 5, 8, 13, ..., so if the number 4 was passed as the argument, 3 
#* would be returned as it is the 4th term in the sequence.

def fibonacci_series(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, number+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci_series(0))
print(fibonacci_series(1))
print(fibonacci_series(2))
print(fibonacci_series(3))
print(fibonacci_series(4))