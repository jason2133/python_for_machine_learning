names = ['Jason', 'Jaeseung', 'Lee', 'The', 'Greatest', 'CEO', 'of', 'the', 'World']

print(names)

a = 'KoreaUniv,SeoulNatlUniv,YonseiUniv'

print(a.split(","))
# ,를 기준으로 리스트를 나눈다

print(a.split("o"))
# o를 기준으로 리스트를 나눈다

b, c, d = a.split(",")
print(b)
print(c)
print(d)

# b, c, d는 ,를 기준으로 나눈 것에 대해 각각 배당을 해준다 그리고 그 b c d를 프린트해준다.

# Split 함수는 String Type의 값을 나눠서 List 형태로 변환시켜준다.