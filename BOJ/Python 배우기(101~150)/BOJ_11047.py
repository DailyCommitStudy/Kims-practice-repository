n, k = map(int, input().split())
case = sorted([int(input()) for _ in range(n)], reverse=True)
res = 0
for c in case :
    if k//c :
        res += k//c
        k = k%c

print(res)
