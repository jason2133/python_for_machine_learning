def asterisk1(a, *b):
    print(a, b)
    print(type(b))

asterisk1(1, *(2, 3, 4, 5, 6))


def asterisk2(a, b):
    print(a, *b)
    print(type(b))

asterisk2(1, (2,3,4,5,6))


