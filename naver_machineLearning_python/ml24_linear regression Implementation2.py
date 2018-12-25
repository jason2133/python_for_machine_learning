import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\datapython\slr06.csv', 'r')

print(df.head())



# a = open('C:\datapython\slr06.csv')
# reader = csv.reader(a)
# lines = list(reader)
# print(lines)
# 이건 모든 데이터가 리스트 형태로 읽혀지네

# 데이터 읽기 성공 야호!
#          X,Y
# 0  108,392.5
# 1    19,46.2
# 2    13,15.7
# 3  124,422.2
# 4   40,119.4

# raw_X = df["X"].values.reshape(-1, 1)
# y = df["Y"].values
#
# plt.figure(figsize=(10,5))
# plt.plot(raw_X,y, 'o', alpha=0.5)




