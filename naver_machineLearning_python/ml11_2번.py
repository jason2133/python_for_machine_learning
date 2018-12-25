# vector_addition
# vector간 덧셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음

def vector_addition(*a):
    for i in range(len(a) - 1):
        if (len((a)[i])) == (len((a)[i+1])) :
            b = "True"
        else:
            b = "False"

    if b == "True":
        a = [sum(i) for i in zip(*a)]
        # zip : 같은 index에 있는 값을 추출한다
        return a

    elif b == "False" :
        return "ArithmeticError"

print(vector_addition([1, 3], [2, 4], [6, 7]))
print(vector_addition([1, 5], [10, 4], [4, 7]))
print(vector_addition([1, 3, 4], [4], [6,7]))



