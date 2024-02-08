# 수는 -10,000,000 ~ 10,000,000
# 숫자 카드의 개수는 1 ~ 500,000
# 딕셔너리 + sys의 조합..^^ 아무리 시간 제한이 있어도 빠르게 통과 굿~
# 118084LB (ㅋㅋ숫자 크고 많아서 쩔수인듯), 744ms

import sys

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
bag = {}
for i in n:
    if i in bag.keys():
        bag[i] += 1
    else:
        bag[i] = 1

M = int(sys.stdin.readline())
for i in map(int, sys.stdin.readline().split()):
    if i in bag.keys():
        sys.stdout.write(str(bag[i])+" ")
    else:
        sys.stdout.write("0 ")
