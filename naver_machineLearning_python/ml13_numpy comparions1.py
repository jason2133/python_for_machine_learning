import numpy as np

a = np.arange(10)
print(a)

print(np.any(a > 5))
# any : 하나라도 조건에 만족한다면 True

print(np.all(a > 5))
print(np.all(a < 20))
# all : 모두 조건에 만족한다면 True

b = np.array([1, 3, 0], float)
c = np.array([1, 2, 1], float)
print(b > c) # 원소 각각 계산해줌
print(b == c) # 원소 각각 계산해줌
print((b > c).any())

# np.logical
d = np.array([6, 9, 5], float)
print(np.logical_and(d > 0, d < 7))

e = np.array([True, False, True], bool)
f = np.array([False, True, False], bool)
print(np.logical_not(e))
print(np.logical_or(e, f))

g = np.array([1, 2, 3])
print(np.where(g > 1, 58, 69)) # where(condition, TRUE, FALSE)
# g에서 g > 1 먹인다음 True면 58을, False면 69를 프린트해라

h = np.arange(10)
print(np.where(h > 6)) # True인 곳의 Index값을 반환한다

i = np.array([1, np.nan, np.Inf], float)
print(np.isnan(i)) # nan == Not A Number

print(np.isfinite(i)) # finite number, 유한값이냐

j = np.array([1, 2, 4, 5, 8, 78, 23, 3])
print(np.argmax(j))
print(np.argmin(j))
# array내 최댓값 또는 최솟값의 index를 반환함

k = np.array([[1, 2, 4, 7], [9, 88, 6, 45], [9, 76, 3, 4]])
print(np.argmax(k, axis = 0))
print(np.argmin(k, axis = 0))

print(np.argmax(k, axis = 1))
print(np.argmin(k, axis = 1))

# array내 최댓값 또는 최솟값의 index를 반환함





