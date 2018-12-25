# matrix 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def vector_subtraction(*a):
    for i in range(len(a) - 1):
        if (len((a)[i])) == (len((a)[i+1])) :
            b = "True"
        else:
            b = "False"
    return b


def matrix_size_check(*matrix_variables):
    c = 0
    for i in range(len(matrix_variables) - 1):
        if (len((matrix_variables)[i])) == (len((matrix_variables)[i+1])) :
            c = c + 1
        else:
            c = c - 1
    return c


matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_y, matrix_z, matrix_x, matrix_y, matrix_z))
print (matrix_size_check(matrix_x, matrix_w, matrix_y, matrix_z))

# 뭐지 일단 패스
