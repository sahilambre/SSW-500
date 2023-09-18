#Problem 2

def rearrange_digits(num):
    digits = list(str(num))
    
    # bubble sort approach
    for i in range(len(digits)):
        for j in range(len(digits)-i-1):
            if digits[j] > digits[j+1]:
                digits[j], digits[j+1] = digits[j+1], digits[j]
    
    return int(''.join(digits))

print(rearrange_digits(3245672))
print(rearrange_digits(9873746))
print(rearrange_digits(1236547))