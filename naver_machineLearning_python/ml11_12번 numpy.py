import numpy as np

# a는 원소 1부터 6까지 2x3의 모양으로 해주세요!
a = np.arange(1, 7).reshape(2, 3)

# b는 원소 7부터 12까지 3x2의 모양으로 해주세요!
b = np.arange(7, 13).reshape(3, 2)

print(a)
print(b)

# 행렬로 표현하고 싶다면 이렇게 np.array로 표현하면 되구나!
c = np.array([[8,9,10], [11,12,13]])
d = np.array([[14, 15], [16, 17], [18, 19]])

# 행렬 a와 b를 곱해라
print(a.dot(b))

print(c)
print(d)
print(c.dot(d))



