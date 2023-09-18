# problem 1


def piApproximation(iterations):
    x = 0
    sign = 1
    for i in range(iterations):
        den = 2 * i + 1
        # den = 2 * x + 1

        x += sign * (1 / den)
        sign *= -1
    x *= 4
    return x

enterIterations = int(input("No of iterations"))

pi = piApproximation(enterIterations)

print("the approximatoin of pi is", enterIterations, pi)
