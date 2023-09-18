
#!Problem 5

import numpy as np
#a
X = np.array([0,0,0,10,0,0,0,0,0,25,0,0,0,12,0,30,0,0]).reshape(2,9)
print(X)
#b
Y = np.sin(X)
print(Y)

#c 
Z = np.random.randint(80, 200, size=(6, 8))
print(Z)

#d 
G = np.random.randint(50, 180, size=(8, 9))
print(G)

#e
F = np.dot(Z, G)
print(F)

