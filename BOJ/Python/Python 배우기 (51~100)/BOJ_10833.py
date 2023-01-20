res = 0
for _ in range(int(input())) :
    s, a = map(int, input().split())
    res += a%s
print(res)