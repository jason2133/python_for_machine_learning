import numpy as np

# 벡터 shape
a = np.array([1, 2, 3, "4"], float)
print(a)
print(a.shape)

# 행렬 shape
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(np.array(b, int).shape)

# 3차원 Tensor shape
c = [[[17, 18, 19, 20], [17, 18, 19, 20], [17, 18, 19, 20]],
     [[17, 18, 19, 20], [17, 18, 19, 20], [17, 18, 19, 20]],
     [[17, 18, 19, 20], [17, 18, 19, 20], [17, 18, 19, 20]],
     [[17, 18, 19, 20], [17, 18, 19, 20], [17, 18, 19, 20]]
     ]

print(np.array(c, int).shape)
# 이걸 하면 (4, 3, 4)가 출력됨
# 처음의 4는 number of dimension. 행렬의 개수랄까
# 두번째의 3은 행렬의 Row 개수에 해당함
# 세번째의 4는 행렬의 Column 개수에 해당함

# Array dtype
# 각 element가 차지하는 memory의 크기를 반환함
d = (np.array([[1, 2, 3], [4.5, 5, 6]], dtype = int))
print(d)

e = (np.array([[1, 2, 3], [4.5, "5", "6"]], dtype = np.float32))
print(e)

# Array dtype
# nbytes - ndarray object의 메모리 크기를 반환함

f = (np.array([[1, 2, 3], [4.5, "5", "6"]], dtype = np.float(32)).nbytes)
print(f)

g = (np.array([[1, 2, 3], [4.5, "5", "6"]], dtype = np.int8).nbytes)
print(g)

h = (np.array([[1, 2, 3], [4.5, "5", "6"]], dtype = np.float(64)).nbytes)
print(h)



