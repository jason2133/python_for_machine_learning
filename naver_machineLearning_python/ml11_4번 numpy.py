# broadcasting
# Shape이 다른 배열 간 연산을 지원하는 기능

import numpy as np

# a는 원소 1부터 6까지 1x6의 모양으로 해주세요!
a = np.arange(1, 7).reshape(6)

# Vector - Scalar 곱셈
print(a * 3)


