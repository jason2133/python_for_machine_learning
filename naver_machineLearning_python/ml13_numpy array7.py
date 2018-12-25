# ones and zeros and empty

import numpy as np

# zeros : 0으로 가득찬 ndarray 생성
a = np.zeros(shape = (10,), dtype = np.int8)
print(a)

b = np.zeros((2, 5))
print(b)

# ones : 1로 가득찬 ndarray 생성
c = np.ones(shape = (10,), dtype = np.int8)
print(c)

d = np.ones((2,5))
print(d)

# empty : shape만 주어지고 비어있는 ndarray가 만들어짐
# memory initialization이 되지 않음

e = np.empty(shape = (10,), dtype = np.int8)
print(e)

f = np.empty((3, 5))
print(f)


