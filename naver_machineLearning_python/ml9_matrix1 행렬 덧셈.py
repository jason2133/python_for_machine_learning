# C = A + B
# A = [ 3 6 ]   B = [ 5 8 ]
#     [ 4 5 ]       [ 6 7 ]

a = [[3, 6], [4, 5]]
b = [[5, 8], [6, 7]]

c = [[sum(row) for row in zip(*t)] for t in zip(a, b)]

print(c)

