#Problem 3

def is_fibonacci(n):
    if n in [0, 1]:
        return True

    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

print(is_fibonacci(7))
print(is_fibonacci(0))
print(is_fibonacci(144))
print(is_fibonacci(701408733))
print(is_fibonacci(701408743))