a = ["A", "B", "C"]
b = ["D", "E", "A"]

c = [i+j for i in a for j in b]
print(c)
# 1차원 배열로 합쳐서 프린트됨


d = [[i+j for i in a] for j in b]
print(d)
# 2차원 배열로 합쳐서 프린트됨



