M, cur = 0, 0
for _ in range(4) :
    a, b = map(int, input().split())
    cur += b-a
    if cur > M : M = cur
print(M)