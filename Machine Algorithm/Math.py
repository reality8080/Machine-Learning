import pandas
import matplotlib.pyplot as plt
import numpy

X=pandas.read_csv("D:/2024-2025/HK2/Trí tuệ nhân tạo/Thực hành/Machine Algorithm/diabetes.csv", header=0)
X.columns=X.columns.str.strip()
numpy.set_printoptions(suppress=True)
