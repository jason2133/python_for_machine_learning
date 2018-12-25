# numpy index
import numpy as np

a = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
print(a > 3)
print(a[a > 3]) # 조건이 True인 index의 element만 추출함

b = a > 3
print(a[b])
# 위 둘이 같은 말. 같은 표현이니라!

# Boolean Index
c = np.array([
    [5, 8, 6, 9, 10, 11],
    [6, 9, 7, 2, 3, 5],
    [50, 8, 1, 6, 7, 8],
    [6, 7, 9, 8, 7, 4],
    [7, 8, 9, 10, 11, 12],
])

d = c < 10
print(d.astype(np.int))
# d가 조건이고, 저 조건에서 True라면 1을, False라면 0을 반환한다!

# Fancy Index
e = np.array([2, 4, 6, 8], float)
f = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 integer로 선언한다
print(e[f]) # bracket index, f 배열의 값을 index로 하여 e의 값들을 추출함
print(e.take(f)) #위에 bracket index와 같은 효과

# Fancy Index
# matrix 형태의 데이터도 가능
g = np.array([[1, 4], [9, 16]], float)
# 위 행렬의 모양은
# [ 1 4  ]
# [ 9 16 ]

h = np.array([0, 0, 1, 1, 0], int)
i = np.array([0, 1, 1, 1, 1], int)
print(g[h, i])
# 프린트해라. 무엇을?
# [0, 0]이랑 [0, 1]이랑 [1, 1]이랑 [1, 1]이랑 [0, 1]을!
# 즉 1 4 16 16 4 이겠지

# loadtxt랑 savetxt는
# Text type의 데이터를 읽고 저장하는 기능이다!





