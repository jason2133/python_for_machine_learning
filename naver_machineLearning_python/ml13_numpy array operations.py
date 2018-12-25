import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], float)
# a의 행렬 모양
# [ 1 2 3 ]
# [ 4 5 6 ]

print(a + a)
print(a - a)
print(a * a) # 요건 특이하게 같은 위치에 있는 값들끼리의 곱이다. 행렬 사이의 곱이 아니라.
# Element-Wise Operations

b = np.arange(1, 19).reshape(3, 6)
print(b * b)

# 행렬 사이의 곱셈은 Dot Product를 사용한다. Dot 함수를 사용함
c = np.arange(1, 7).reshape(2, 3)
# 행렬 c의 모양
# [ 1 2 3 ]
# [ 4 5 6 ]

d = np.arange(7, 13).reshape(3, 2)
# 행렬 d의 모양
# [ 7  8  ]
# [ 9  10 ]
# [ 11 12 ]

print(c.dot(d))
# 행렬 c와 d 사이의 곱셈이다 즉,
# [ 1 2 3 ]  * [ 7 8   ]   ==  [ 1*7 + 2*9 + 3*11       1*8 + 2*10 + 3*12 ]
# [ 4 5 6 ]    [ 9 10  ]       [ 4*7 + 5*9 + 6*11       4*8 + 5*10 + 6*12 ]
#              [ 11 12 ]

# 행렬의 Transpose 먹이는 것.
# transpose나 T attribute를 사용한다
e = np.arange(1, 49).reshape(6, 8)
print(e)
print(e.transpose())
print(e.T)
# e.transpose와 e.T는 같은 표현이다. 행렬의 Transpose다.

print(e.T.dot(e))

# Broadcasting : Shape이 다른 배열 간 연산을 지원하는 기능
f = np.array([[1, 2, 3], [4, 5, 6]], float)
g = 5
print(f + g)
print(f - g)
print(f + g)
print(f / 5)
print(f // 0.2)
print(f ** 2)

h = np.arange(1, 13).reshape(4, 3)
i = np.arange(10, 40, 10) # 등차수열. parameter가 3개 있다. 이건 등차수열이다. 첫항이 10인, 공차가 10인 등차수열이지
# 즉 i의 구성요소는 10 20 30이라는 소리다
print(h + i)








