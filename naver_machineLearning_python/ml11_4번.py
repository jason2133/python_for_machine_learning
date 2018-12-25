# a = [sum(i) for i in zip(*a)]

# 1. 별이 위 아래 둘 다 있는 경우
# def scalar_vector_product(alpha, *vector_variable):
#     return [alpha * i for i in zip(*vector_variable)]
#
#
# print (scalar_vector_product(5, [1,2,3]))
# print (scalar_vector_product(3,[2,2]))
# print (scalar_vector_product(4,[1]))
#
# [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3)]
# [(2, 2, 2), (2, 2, 2)]
# [(1, 1, 1, 1)]

# 2. 별이 위에 하나만 있고 아래에는 없는 경우
# def scalar_vector_product(alpha, *vector_variable):
#     return [alpha * i for i in zip(vector_variable)]
#
#
# print (scalar_vector_product(5, [1,2,3]))
# print (scalar_vector_product(3,[2,2]))
# print (scalar_vector_product(4,[1]))
#
# [([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])]
# [([2, 2], [2, 2], [2, 2])]
# [([1], [1], [1], [1])]


def scalar_vector_product(alpha, vector_variable):
    return [sum(alpha * i) for i in zip(vector_variable)]

print (scalar_vector_product(5, [1,2,3]))
print (scalar_vector_product(3,[2,2]))
print (scalar_vector_product(4,[1]))
