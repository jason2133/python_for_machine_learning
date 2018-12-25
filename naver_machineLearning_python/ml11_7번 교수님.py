# matrix_addition
# matrix간 덧셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음

def matrix_size_check(*matrix_variables):
    return (all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and
            all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables]))

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        return ArithmeticError
    else:
        return [[sum(row) for row in zip(*matrix)]
                for matrix in zip(*matrix_variables)]

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]




