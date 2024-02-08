def func() : return sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])

print(func(), func())