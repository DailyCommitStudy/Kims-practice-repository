# 	42384kB	928ms

N, M = map(int, input().split())
S = {input() for _ in range(N)}
case = [input() for _ in range(M)]

answer = 0
for c in case:
    if c in S:
        answer += 1

print(answer)

