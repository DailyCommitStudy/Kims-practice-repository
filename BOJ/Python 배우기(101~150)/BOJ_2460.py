M, cur = 0, 0
for _ in range(10) :
    a, b = map(int, input().split())
    cur += b-a
    if cur > M : M = cur
print(M)