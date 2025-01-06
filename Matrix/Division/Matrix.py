import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
# print("Phép chia cùng M*N:\n",A.(B))
# Phải nghịch đảo B
b=np.linalg.pinv(A)
print("Giá trị nghịch đảo: ",b)
# Giá ttrij nghịc đảo phải khác 0
b=np.linalg.pinv(B)
print("Phép chia ma trận cùng M*N:\n",A*b)
# Lưu ý chỉ có thể cộng với các ma trận cùng là M*N
