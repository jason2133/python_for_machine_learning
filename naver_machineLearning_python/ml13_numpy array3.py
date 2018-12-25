import numpy as np

# reshape

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = (np.array(a).shape)
print(b)
# 저 a의 구성이 어떤지 알려줌
# 출력되는 것은 (2, 4)
# 즉 row가 2고 column이 4인 행렬을 프린트해준다는거지

c = (np.array(a).reshape(8,))
print(c)
# 원래 갖고 있던 행렬을 다시 재배열
# 8개로 쭉 straight하게 프린트해준다는거지

d = (np.array(a).reshape(8,).shape)
print(d)
# 위에 c에서 8개로 쭈욱 straight하게 프린트해준거의 shape가 어떤지 표현해주는 것임
# c에서 8개로 프린트되었으니 shape는 8개겠지

# reshape
# array의 size만 같다면 다차원으로 자유로이 변형가능
e = (np.array(a).reshape(2,4).shape)
print(e)

f = (np.array(a).reshape(-1, 2).shape)
print(f)
# -1 : size를 기반으로 row 개수 설정

g = (np.array(a).reshape(2, 2, 2))
print(g)

h = (np.array(a).reshape(2, 2, 2).shape)
print(h)

# flatten : 다차원 array를 1차원 array로 변환
i = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
j = np.array(i).flatten()
print(j)

# 원래 4*4 형태의 행렬로 되어있던 것을 1차원으로 바꿔준다는 것이지









