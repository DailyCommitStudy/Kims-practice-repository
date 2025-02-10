'''
"17" -> 1, 7 로 만들 수 있는 숫자
permutations()\
'''

# import itertools

# # 소수 판별 함수
# def check(num):
#     if num in [0, 1]: return False

#     for n in range(2, num):
#         if num%n==0:
#             return False
        
#     return True

# def solution(string):
#     numbers = list(map(int, string))

#     answer = set()
#     for i in range(1, len(numbers)+1):
#         # 순열 함수로 숫자 조합 탐색
#         for perm in itertools.permutations(numbers, i):
#             num = int(''.join(map(str,perm)))
#             if check(num):
#                 answer.add(num)
#     return len(answer)


# print(solution("011"))

'''
테스트 1 〉	통과 (0.33ms, 10.2MB) => (0.40ms, 10.4MB)
테스트 2 〉	통과 (186.01ms, 10.4MB) => (0.40ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.5MB) => (0.04ms, 10.3MB)
테스트 4 〉	통과 (151.68ms, 10.3MB) => (10.41ms, 10.3MB)
테스트 5 〉	통과 (30.53ms, 10.4MB) => (23.67ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB) => (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.52ms, 10.3MB) => (0.18ms, 10.4MB)
테스트 8 〉	통과 (23.47ms, 10.4MB) => (29.12ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.3MB) => (0.04ms, 10.4MB)
테스트 10 〉통과 (3050.66ms, 10.3MB) => (2251.65ms, 10.4MB)
테스트 11 〉통과 (87.45ms, 10.2MB) => (79.68ms, 10.4MB)
테스트 12 〉통과 (2.67ms, 10.3MB) => (0.92ms, 10.3MB)
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

    case = list()
    answer = 0
    for i in range(1, len(numbers)+1):
        # 순열 함수로 숫자 조합 탐색
        for perm in itertools.permutations(numbers, i):
            num = int(''.join(map(str,perm)))
            if num not in case and check(num):
                case.append(num)
                answer += 1
                
    return answer


print(solution("011"))