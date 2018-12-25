a = "Hello"
b = "World"

c = [i + j for i in a  for j in b]
print(c)
# for문 i를 먼저 시행하기에 그걸 먼저 시행해서 고정 시켜놓은 다음
# for문 j를 시행하여 그에 대응시켜준다.

# 문자열 안에 있는거 그대로 시행되기에 개수는 5 * 5 = 25겠지.
# for문을 연달아 썼고, 이건 1차원 배열이다.




