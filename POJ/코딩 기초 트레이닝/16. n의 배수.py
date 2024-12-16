def solution(num, n):
    return 1 if num%n==0 else 0

# 다른 사람의 풀이
def solution(num, n):
    return int(not(num % n))