a = 'Jason is the greatest CEO of the world He will innovate get your crayon'.split()

print(a)

b = [[i.upper(), i.lower(), len(i)] for i in a]

# 그냥 print(b)를 먹여도 되는데 이럴 경우
# 리스트들이 한줄로 가로로 쭈우우욱 프린트된다

for i in b:
    print(i)

# 이렇게 for문을 활용하는 이유는
# 각 리스트를 한줄에 하나씩 프린트하기 위해서다.





