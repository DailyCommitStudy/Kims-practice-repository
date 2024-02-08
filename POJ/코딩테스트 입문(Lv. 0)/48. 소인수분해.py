# 구글링의 힘을 좀 빌렸네/... ^^
def solution(n):
    a = 2
    answer = set()
    while a <= n:
        if n % a == 0:
            answer.add(a)
            n /= a
        else:
            a += 1

    return list(sorted(answer))