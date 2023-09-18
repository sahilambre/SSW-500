
#! Question 9
def approximate_pi(iterations):
    approx_pi = 0
    flag = 1
    # for(i in range(1, iterations, 2))
    for i in range(1, iterations*2, 2):
        term = 1 / i
        approx_pi += flag * term
        flag *= -1

    approx_pi *= 4


    return approx_pi


num_iterations = int(input("Enter the number of iterations for pi approximation: "))
approximated_pi = approximate_pi(num_iterations)

print("Approximated value of pi:", approximated_pi)
