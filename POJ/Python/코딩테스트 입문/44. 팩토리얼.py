def solution(n):
    # b = a!
    a, b = 1, 1
    while b <= n:
        b = a * b
        a += 1

    return a - 2