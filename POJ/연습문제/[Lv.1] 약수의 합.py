# 약수의 합은 공식을 이용하려면 소인수분해 후 계산해야 함
# 굳이 그럴 필요는 없을듯
# 그냥 반복문으로 약수를 구해 리스트에 저장 후 합한다

def solution(n):
    return sum([i for i in range(1, n+1) if n%i==0])

## 다른 사람 코드
'''
16이면 1, 2, 4, 8, 16
# 8까지 검사하므로 1, 2, 4, 8 + 16
# 1, n까지 검사할 필요 없이 2 ~ n//2 로 범위를 줄인다라..
똒똑하네 ㄷㄷ..
'''
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
