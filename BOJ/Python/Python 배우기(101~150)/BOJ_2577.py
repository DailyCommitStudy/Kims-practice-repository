from functools import reduce

s = str(reduce(lambda x, y: x * y, [int(input()) for _ in range(3)]))
for i in range(10):
    print(s.count(str(i)))