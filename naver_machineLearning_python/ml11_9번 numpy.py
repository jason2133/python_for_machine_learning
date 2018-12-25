import numpy as np

# a는 원소 1부터 6까지 2x3의 모양으로 해주세요!
a = np.arange(1, 7).reshape(2, 3)

# b는 원소 7부터 12까지 3x2의 모양으로 해주세요!
b = np.arange(7, 13).reshape(3, 2)

# 밑에 둘 다 행렬의 Transpose를 먹이는 것으로 같음!
print(a.transpose())
print(b.T)





