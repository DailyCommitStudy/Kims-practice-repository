# 42924KB / 88ms

import sys

N, M = map(int, sys.stdin.readline().split())
h = {sys.stdin.readline().rstrip() for _ in range(N)}
s = {sys.stdin.readline().rstrip() for _ in range(M)}

# 듣보잡 찾기 + 사전순 출력
hs = sorted(h&s)
sys.stdout.write(f"{len(hs)}\n")
for r in hs:
    sys.stdout.write(r+'\n')