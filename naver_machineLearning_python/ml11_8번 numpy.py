import numpy as np

# a는 원소 1부터 6까지 2x3의 모양으로 해주세요!
a = np.arange(1, 7).reshape(2, 3)

# b는 원소 7부터 12까지 2x3의 모양으로 해주세요!
b = np.arange(7, 13).reshape(2, 3)

print(a - b)
