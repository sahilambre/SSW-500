
#* Python’s pow function returns the result of raising a number to a given power. Define a 
#* function expo that performs this task. The first argument of this function is the number, and 
#* the second argument is the exponent (non-negative numbers only). You may use either a loop 
#* or a recursive function in your implementation.  
#* CAUTION: do not use Python’s ** operator or pow function in this exercise! 


def exponent_function(num, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        result = num
        for i in range(1, exp):
            result *= num
        return result

print(exponent_function(1,0))
print(exponent_function(0,0))
print(exponent_function(2,4))
print(exponent_function(-10,3))
print(exponent_function(0,2))
