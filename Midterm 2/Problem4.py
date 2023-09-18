
#!Problem 4 

import numpy as np

LHS = np.array([[2, 2, -1, 1], [4, 3, -1, 2], [8, 5, -3, 4], [3, 3, -2, 2]])
RHS = np.array([4, 6, 12, 6])

answer = np.linalg.solve(LHS, RHS)

print(answer)
