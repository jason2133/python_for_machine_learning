# broadcasting
# Shape이 다른 배열 간 연산을 지원하는 기능

import numpy as np

# a는 원소 1부터 6까지 2x3의 모양으로 해주세요!
a = np.arange(1, 7).reshape(2, 3)

# b는 원소 7부터 12까지 2x3의 모양으로 해주세요!
b = np.arange(7, 13).reshape(2, 3)

# Matrix - Scalar 곱셈
print(a * 3)

# 밑에부터는 추가요소지!
# Matrix - Scalar 덧셈
print(a + 3)

# Matrix - Scalar 뺄셈
print(a - 3)

# Matrix - Scalar 곱셈
print(a * 3)

# Matrix - Scalar 나눗셈
print(b / 3)

# Matrix - Scalar 몫
print(b // 3)

# Matrix - Scalar 제곱
print(a ** 2)


