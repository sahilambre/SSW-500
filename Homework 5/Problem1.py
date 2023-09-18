#Problem 1

def exponent(num, exp):
    result = 1
    for element in range(exp):
        result *= num 
    return result

print(exponent(2,3))
print(exponent(5,2))
print(exponent(10,0))