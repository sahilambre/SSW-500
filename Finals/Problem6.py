
#! Question 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = int(input("Starting Range: "))
end = int(input("Ending Range: "))

prime_numbers = []
for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers in the asked range:", prime_numbers)
