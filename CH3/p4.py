import numpy as np

A = np.array([[1,1,1,1],[2,-1,2,-1],[3,2,-1,2],[1,3,2,-1]])
B= np.array([10,3,11,9])

Ainv=np.linalg.inv(A)
print(f"역행렬 {Ainv}")
s=Ainv@B
w,x,y,z=s
print(f"w = {w:.1f}, x = {x:.1f}, y = {y:.1f}, z = {z:.1f}")
print(np.matmul(A, s))
