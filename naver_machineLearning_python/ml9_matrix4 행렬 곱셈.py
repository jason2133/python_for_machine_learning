matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1,4], [2, 5], [3, 6]]

c = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]

print(c)


