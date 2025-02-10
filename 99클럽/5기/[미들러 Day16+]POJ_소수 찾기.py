'''
"17" -> 1, 7 로 만들 수 있는 숫자
permutations()\
'''

import itertools

# 소수 판별 함수
def check(num):
    if num in [0, 1]: return False

    for n in range(2, num):
        if num%n==0:
            return False
        
    return True

def solution(string):
    numbers = list(map(int, string))

    answer = set()
    for i in range(1, len(numbers)+1):
        # 순열 함수로 숫자 조합 탐색
        for perm in itertools.permutations(numbers, i):
            num = int(''.join(map(str,perm)))
            if check(num):
                answer.add(num)
    return len(answer)


print(solution("011"))