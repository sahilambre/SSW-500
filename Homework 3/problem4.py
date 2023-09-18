number = int(input("Enter number of terms "))

a, b = 0, 1
fib_seq = [a, b]

for i in range(2, number):
    c = a + b
    fib_seq.append(c)
    a, b = b, c

print("Fibonacci sequence to", number, "numbers :")
print(fib_seq)

