# 예산이 남더라도? 최대한 다양한 부서에 지원할 수 있어야 한다

# 첫 번째 풀이
# 답은 충분히 낼 수 있었으나 시간 초과 문제.. 새로운 로직 생각 필요
from itertools import combinations as cb

def solution(d, budget):
    for i in range(len(d), -1, -1):
        for j in cb(d, i):
            if sum(j) <= budget:
                return i

# 다른 사람 코드 참고해서 푼 것
# 솔직히 아직까지 정확히 이해가 안됨.ㅠㅠ 이게 모든 경우를 포괄할 수 있어 ㄹㅇ로?

# 새로운 로직?
# 모든 부서에 대해 작은 예산부터 빼본다
# 이때 마이너스가 되면 return한다

def solution(d, budget):
    d.sort()

    for i, n in enumerate(d):
        budget -= n

        if budget < 0:
            return i

    return len(d)