# index는 O(N^2) -> 시간초과 -> 딕셔너리로 해결 (1908ms)
# 각 값마다 인덱스를 찾는 방법?

import sys

N = int(input())
case = list(map(int,(sys.stdin.readline().split())))
uni = sorted(set(case))

d = { k : v for k, v in zip(uni, range(N))}

for c in case:
    print(d[c], end=' ')