
#! Problem 2 

import time

#* Linear Approach
start_linear = time.time()
def power_linear(base, exp):
    result = 1
    for element in range(exp):
        result *= base
    return result
end_linear = time.time()
time_linear = end_linear - start_linear

#* Recursive Approach
start_recursive = time.time()
def power_recursive(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power_recursive(base, exp - 1)

end_recursive = time.time()
time_recursive = end_recursive - start_recursive

#TODO: Check complexity
# print(power_linear(12789,89), "Time elapsed: ", time_linear)
# print(power_recursive(12789,89), "Time elapsed: ", time_recursive)

print(power_linear(5,5))
print(power_recursive(5,1))

#?Answer: 
#* When comaparing the time complexities of the above two functions, recursice function is better suited for large values.
#* As it takes less time to calculate the result as the exponent grows
#* On the other hand, for small values of exponent, the linear function may be faster, because the overhead of recursion in the recursive function may slow it down
#* Therefore, the choice of which function to use depends on the specific context, and specifically on the size of the exponent.