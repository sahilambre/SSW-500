def prime_check(n):
    if n < 2:
    # if n =< 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
    # for i in range(1, int(n ** 2) + 1):
        if n % i == 0:
            return False
    return True

list = []
for element in range(1, 101):
    if prime_check(element):
        list.append(element)
print(list)
