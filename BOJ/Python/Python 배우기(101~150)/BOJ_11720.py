from functools import reduce
n = input()
print(reduce(lambda x, y : int(x)+int(y), input()))