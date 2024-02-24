# 정석적 코드
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(set(answer))

# 아맞다 콜라보레이터
from itertools import combinations as cb

def solution(numbers):
    return sorted({sum(i) for i in cb(numbers, 2)})