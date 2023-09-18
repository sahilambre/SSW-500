
#*Write a program to check if the values in myDict are prime or not. If a prime number is found, 
#*the program should print a text message including the corresponding key of the prime number. 
#*myDict = {“A”: 11, “B”: 4, “C”: 7, “D”: 15, “E”: 1} 
 
#*Hint: a natural number is called a prime number (or a prime) if it is greater than 1 and cannot 
#*be written as the product of two smaller natural numbers. Prime numbers are divisible only by 
#*the number 1 or itself. For example, 2, 3, and 5 are prime numbers. 

# myDict = {"key 1": 12, "key 2": 4, "key 3": 9, "key 4": 11, "key 5": 1, "key 6": 0, "key 7": 2, "key 8": 7}
myDict = {"A": 11, "B": 4, "C": 7, "D": 15, "E": 1} 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

for key, value in myDict.items():
    if is_prime(value):
        print(f"{key} has a prime value: {value}")
