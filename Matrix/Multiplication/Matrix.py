import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Phép nhân cùng M*N:\n",A.dot(B))
# Lưu ý chỉ có thể cộng với các ma trận cùng là M*N
n=int(input("Hãy nhập n mong muốn: "))
print("Phép nhân với một số: ", A*n)

C=np.array([[1,2,3],[4,5,6],[7,8,9]])
DD=np.array([1,2,3])
print("Phép nhân giữa ma trận và vector:\n",A*B)

# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.array([[1,2,3],[4,5,6]])
# print("Phép nhân khácác M*N:\n",A.dot(B))