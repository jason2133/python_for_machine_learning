# arrange

import numpy as np

a = np.arange(30)
print(a)

b = np.arange(0, 5, 0.5)
print(b)

c = np.arange(30).reshape(5, 6)
print(c)
# range 30까지 있는 것을
# row 5와 column 6의 모양의 행렬로 프린트해라

d = np.arange(30).reshape(-1, 5)
print(d)
# range 30까지 있는 것을
# -1이라는 말은 니가 알아서 해라~ 이소리인데,
# 뒤에 5를 붙임으로써 row가 5인 것으로
# 니가 알아서해라~

# 위에 c와 d는 같음







