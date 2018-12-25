# vector_subtraction
# vector간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음

def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x
        for x in [len(vector) for vector in vector_variables[1:]])

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2 - sum(elements)
            for elements in zip(*vector_variables)]

print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]

