# matrix_transpose
# matrix의 transpose을 구하여 결과를 반환함, 단 입력되는 matrix의 크기는 일정하지 않음

def matrix_transpose(matrix_variable):
    return [ [element for element in row] for row in zip(*matrix_variable)]

# 실행결과
matrix_w = [[2, 5], [1, 1], [2, 2]]
print(matrix_transpose(matrix_w))
