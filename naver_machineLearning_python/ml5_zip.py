alist = ['A', 'B', 'C']
blist = ['D', 'E', 'F']

for a, b in zip(alist, blist):
    print(a, b)
# alist와 blist에서 같은 index값에 해당하는 value들이 같이 출력된다.

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
# 요것도 마찬가지로 a, b, c에서 같은 index에 해당하는 value들이 같이 출력된다
# 따라서 1, 10, 100이 한팀 / 2, 20, 200이 한팀 / 3, 30, 300이 한팀이겠지

d = [sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(d)
# sum은 그 값을 합친다는 소리다
# 따라서 zip 안에 있는 원소들을 각각 sum(x) 합친다는 소리
# 111, 222, 333이 답이겠다.




