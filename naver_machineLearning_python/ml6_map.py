a = [1, 2, 3, 4, 5]
b = lambda x : x ** 2
print(list(map(b, a)))

c = lambda x, y : x + y
print(list(map(c, a, a)))

print(list(
    map(
        lambda x : x ** 2 if x % 2 == 0
        else x,
        a
    )
))


