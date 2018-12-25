# is_matrix_equal
# 	비교가 되는 n개의 matrix가 서로 동치인지 확인하여 True 또는 False를 반환함

def is_matrix_equal(*matrix_variables):
    return all([all([len(set(row)) == 1 for row in zip(*matrix)])
                for matrix in zip(*matrix_variables)] )

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]

print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True
