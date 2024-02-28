## 간단히 피보나치 수 구하는 로직 구현

def solution(n):
    if n <= 2:
        return 1

    a, b = 1, 1
    for i in range(2, n):
        a, b = a + b, a

    return a % 1234567