# scalar_vector_product
# 하나의 scalar 값을 vector에 곱함, 단 입력되는 vector의 크기는 일정하지 않음

def scalar_vector_product(alpha, vector_variable):
    return [alpha*element for element in vector_variable]

print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]

