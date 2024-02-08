# 대칭 차집합 A-B + B-A
# 81100KB	272ms

import sys

a, b = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

print(f"{len(A-B) + len(B-A)}")