

#!Question 8
#! Iterative method

def fibonacci_iterative(n):
    fibonacci_seq = [0, 1]

    while len(fibonacci_seq) < n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    return fibonacci_seq



#!recursive mthod 

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_seq = fibonacci_recursive(n-1)
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
        return fibonacci_seq


n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("fibo iterative", fibonacci_iterative(n))
print("fibo recursive", fibonacci_recursive(n))