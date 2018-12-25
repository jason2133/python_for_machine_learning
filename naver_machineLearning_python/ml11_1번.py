# vector_size_check
# vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함

def vector_size_check(*a):
    for i in range(len(a) - 1):
        if (len((a)[i])) == (len((a)[i+1])) :
            b = "True"
        else:
            b = "False"
    return(b)

print(vector_size_check([1, 3, 4], [4], [6,7]))
print(vector_size_check([1,2,3], [2,3,4], [5,6,7]))
print(vector_size_check([1, 3], [2,4], [6]))


def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x
        for x in [len(vector) for vector in vector_variables[1:]])

print(vector_size_check([1, 3, 4], [4], [6,7]))
print(vector_size_check([1,2,3], [2,3,4], [5,6,7]))
print(vector_size_check([1, 3], [2,4], [6]))

# a = ([1,2,3], [2,3], [5])
# print(*a)
# print(len(a))
#
# for i in range(len(a) - 1):
#     if (len((a)[i])) == (len((a)[i+1])) :
#         b = "True"
#     else:
#         b = "False"
#
# print(b)







