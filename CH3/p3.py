import numpy as np

A = np.array([[1,2,3],[10,-1,-5],[6,7,5]])
i=np.eye(A.shape[0],A.shape[1])
r=np.linalg.matrix_power(A,3)-5*np.linalg.matrix_power(A,2)-4*A-98*i
print(r)
