# identity
# 단위 행렬 i 행렬을 생성함
# 즉 i 개수만큼 대각선에는 1이고, 나머지는 다 0인 행렬을 말하는거지

import numpy as np

print(np.identity(n = 3, dtype = np.int8))
print(np.identity(n = 10))

# eye
# 대각선이 1인 행렬에서
# k값의 시작 index의 변경이 가능하다!

print(np.eye(N = 3, M = 5, dtype = np.int8))
print(np.eye(5))
print(np.eye(3, 5, k = 2)) # 여기서 k가 start index다!

# diag
# 대각 행렬의 값을 추출함

a = np.arange(9).reshape(3, 3)
print(np.diag(a))

print(np.diag(a, k = 2))
print(np.diag(a, k = 1))
print(np.diag(a, k = 0))

# random sampling
# 데이터 분포에 따른 sampling으로 array를 생성함

print(np.random.uniform(0, 1, 10).reshape(2, 5)) # 균등분포
print(np.random.normal(0, 1, 10).reshape(2, 5)) # 정규분포






