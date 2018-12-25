# Operation Functions
# 여기서는 Python의 Numpy에 있는 호출해서 사용하는 여러 함수들에 대해 이야기해보고자 해요!

import numpy as np

# sum : 시그마랑 같은 말. 값들을 합친다!
a = np.arange(1, 11)
print(a)
print(a.sum(dtype=float))

# axis : 축
# 행렬 내가 공부를 r이랑 c로 공부했자나
# r : axis = 0
# c : axis = 1
# 행렬이 딱 하나일때에는 위와 같이 axis 설정을 해줌
# 이렇게 표현하면 좋을듯!

b = np.arange(1, 13).reshape(3, 4)
print(b)

print(b.sum(axis = 0))
print(b.sum(axis = 1))

# axis 넣어주면 축을 기준으로 다 합침!

# axis가 3개일 경우
# 개수 : axis = 0
# r : axis = 1
# c : axis = 2

# c = np.arange(1, 26).reshape(5, 5)
# print(c.sum())

print(b.mean())
print(b.mean(axis=0))
print(b.mean(axis=1))

print(b.std())
print(b.std(axis=0))
print(b.std(axis=1))

# c = np.array([1, 2, 3])
# d = np.array([4, 5, 6])
# print(np.vstack(c, d))
#
# e = np.array([[1], [2], [3]])
# f = np.array([[4], [5], [6]])
# print(np.hstack(e, f))






