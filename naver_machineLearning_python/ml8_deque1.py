from collections import deque

a = deque()

for i in range(5):
    a.append(i)
print(a)

a.appendleft(10)
print(a)

a.rotate(2)
print(a)

a.rotate(2)
print(a)

print(deque(reversed(a)))

a.extend([5, 6, 7])
print(a)

a.extendleft([5, 6, 7])
print(a)



