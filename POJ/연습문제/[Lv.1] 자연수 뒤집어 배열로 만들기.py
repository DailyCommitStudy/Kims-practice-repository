## 내가 푼 코드

def solution(n):
    return list(map(int, str(n)))[::-1]

## 다른 사람이 푼 코드
def digit_reverse(n):
    return list(map(int, reversed(str(n))))