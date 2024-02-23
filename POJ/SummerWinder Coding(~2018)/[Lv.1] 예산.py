# 예산이 남더라도? 최대한 다양한 부서에 지원할 수 있어야 한다

# 첫 번째 풀이
# 답은 충분히 낼 수 있었으나 시간 초과 문제.. 새로운 로직 생각 필요
from itertools import combinations as cb

def solution(d, budget):
    for i in range(len(d), -1, -1):
        for j in cb(d, i):
            if sum(j) <= budget:
                return i