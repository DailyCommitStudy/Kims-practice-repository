from math import gcd

def solution(a, b):
    b //= gcd(a, b) # 최대공약수 구하고 약분 뒤 분모 구하기

    ## 나의 풀이
    for i in range(3, b+1):
        if i % 2 == 0 or i % 5 == 0: continue
        if b % i == 0: return 2

    return 1

    ## 다른 사람 풀이
    # while b % 2==0 : b //= 2
    # while b % 5 == 0: b //= 5
    #
    # return 1 if b == 1 else 2

print(solution(12, 21))