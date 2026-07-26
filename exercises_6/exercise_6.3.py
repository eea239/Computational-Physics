import numpy as np

V_plus = 5.0

# A matrix
A = np.array([[4,-1,-1,-1],
              [-1,3,0,-1],
              [-1,0,3,-1],
              [-1,-1,-1,4],
],float)

# v vector
v = np.array([V_plus,0.0,V_plus,0.0],float)

# solution (with numpy function)
solution = np.linalg.solve(A,v)

print(solution)