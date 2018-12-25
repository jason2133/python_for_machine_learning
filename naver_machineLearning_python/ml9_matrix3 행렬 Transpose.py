a = [[1, 2, 3], [4, 5, 6]]
b = [[element for element in t] for t in zip(*a)]
print(b)


