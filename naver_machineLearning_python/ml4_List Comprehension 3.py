a = ["A", "B", "C"]
b = ["D", "E", "A"]
# a, b 각각에서 원소를 정의해주었따

c = [i + j for i in a   for j in b]
print(c)
# 그래서 각 원소를 이렇게 합쳐주었따

d = [i + j for i in a  for j in b  if i != j]
print(d)
# 두 원소가 같다면 원소 합치는 것에 제외한다
# 두 원소가 다르다면 원소 합치는 것에 동원된다

d.sort()
# 정렬해준다
# sort 정렬은 리스트에서만 실행가능한 명령이다

print(d)
# 그걸 프린트해준다



