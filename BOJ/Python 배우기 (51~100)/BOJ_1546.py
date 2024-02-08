# 최댓값 M, 각 점수/M*100
from functools import reduce

n = int(input())
score = list(map(int, input().split()))
m = max(score)
res = 0
for s in score :    res += s/m*100
print(res/n)