import numpy
from matplotlib import pyplot as plt
import pandas
import os

# X=numpy.loadtxt("diabetes.csv", "%.2f",delimiter=',')
# Các thao tác cần có trên một file csvcsv
# Đọc tệp csv và đưa vào DataFrame, chỉ định hàng đầu là tiêu đề
X=pandas.read_csv("D:/2024-2025/HK2/Trí tuệ nhân tạo/Thực hành/Machine Algorithm/diabetes.csv", header=0)
# Loại bỏ khoảng trống giữa các cột
X.columns=X.columns.str.strip()
#Tắt bớt việc dùng kí hiệu khoa học
numpy.set_printoptions(suppress=True)

print(X.head())

print(X.values[11:12,:])
# Tạo folder để lưu trữ nếu cần thiếtthiết
# os.makedirs(os.path.dirname("D:/2024-2025/HK2/Trí tuệ nhân tạo/Thực hành/Machine Algorithm"), exist_ok=True)
# Đọc và ghi 50 dòng đầu tiên
X.iloc[0:50,:].to_csv("D:/2024-2025/HK2/Trí tuệ nhân tạo/Thực hành/Machine Algorithm/output.csv", index=False)
# print(X.values)