names = ['Jason', 'Jaeseung', 'Lee', 'The', 'Greatest', 'CEO', 'of', 'the', 'World']

result = ''

for i in names:
    # for문을 사용했다. in names에서 알 수 있는것처럼 저건 굳이 range(len()) 함수를 쓰지 않아도 된다.
    # for i in names 를 적음으로써 names에 있는 원소들을 print해라 이런식으로 받아들이면 될듯.
    result = result + i

print(result)

