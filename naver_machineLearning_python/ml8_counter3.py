from collections import Counter

a = Counter(a = 4, b = 2, c = 0, d = -2)
b = Counter(a = 1, b = 2, c = 3, d = 4)
a.subtract(b) # a에서 b를 뺀다
print(a)



