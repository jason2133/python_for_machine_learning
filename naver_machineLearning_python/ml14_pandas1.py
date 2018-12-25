import pandas as pd

# 데이터 로딩
# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
# a = pd.read_csv(data_url, sep='\s+', header=None)
# print(a.head())

# Series : DataFrame 중 하나의 Column에 해당하는 데이터의 모음 Object
# DataFrame : Data Table 전체를 포함하는 Object

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

b = [1, 2, 3, 4, 5]
c = Series(data = b)
print(c)
# 이걸 시계열이라고 하는구나. Index와 그에 해당하는 값을 같이 출력해줌 Series
# Index label을 굳이 붙일 필요가 없다!

d = ["a", "b", "c", "d", "e"]
e = Series(data = b, index = d) #index 이름을 d로 지정함.
print(e)

f = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
g = Series(f, dtype = np.float32, name = "ex1") # data의 이름은 ex1이고 data의 타입은 np.float32다!
print(g)

print(g["a"])
g["a"] = 5678
print(g)

print(g.values) # 값 리스트만
print(g.index) # index 리스트만

g.name = "number"
g.index.name = "ex2"
print(g)
# 데이터 이름이랑 index 이름같은거 다 집어넣어서 진행중~

h = {"a": 6, "b" : 7, "c" : 8, "d" : 9, "e" : 10} # 데이터 값을 지정해줌
i = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] # index에는 이러이러한 것이 있다
j = Series(h, index=i) # h와 i를 시계열 Series로 뭉친다
print(j) # 프린트를 해봐라 NaN은 데이터가 없다는 뜻이다








