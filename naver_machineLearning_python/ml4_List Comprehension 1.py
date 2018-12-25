a = []

for i in range(10):
    a.append(i)

print(a)
# 원래 원시적으로ㅋㅋㅋ 하던 append 방식

b = [i for i in range(10)]
print(b)
# a를 b로 이렇게 간소화시켜서 표현시킬 수 있다

c = [i for i in range(10) if i % 2 == 0]
print(c)
# c는 if라는 조건문을 집어넣은 것이다.
# 2의배수



