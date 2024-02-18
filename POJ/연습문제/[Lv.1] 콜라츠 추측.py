# 정석적인 방법
# 내 코드가 가장 나은듯 ㅎ
def solution(num):
    for i in range(500):
        if num == 1:
            return i
        elif num % 2:
            num = num * 3 + 1
        else:
            num //= 2

    return -1

print(solution(1))