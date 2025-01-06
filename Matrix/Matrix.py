import numpy as ny
A=ny.array([[1,2,3],[4,5,6]])
print(A)
print("Các thao tác đơn giản trong ma trận")
print(A[0,0])
print(A[:,0])
print(A[0,:])
print(A[1,1])
print(A[:,1])
print(A[1,:])
# Phía trước là hàng, phía sau là cột
print("\n")

print("Ma trận đơn vị:\n",ny.eye(10))