# indexing

import numpy as np

a = np.array([[1, 2, 3], [4.5, 5, 6]], int)
# 뒤에 int를 붙여주었기에 4.5를 int인 4로 바꿔줌

print(a)
print(a[0, 0])
print(a[0][0])

a[0, 0] = 12
print(a)

a[0][0] = 5
print(a)

# List와 달리 여기 2차원 배열에서는
# [0][0] == [0, 0]
# 기억해라! 우리의! 붉은! 함성을!
# 들어라 보아라 기억하라
# ㅋㅋㅋㅋㅋㅋㅋ새벽코딩ㅋㅋㅋㅋㅋㅋ해탈잼


