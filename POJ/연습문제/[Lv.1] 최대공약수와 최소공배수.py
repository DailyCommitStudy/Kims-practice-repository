# 단순하게 이론 중심으로 적은 내 코드
# 다른 사람 코드 + 유클리드 호제법 공부해보기
def solution(n, m):
    answer = [0, 0]

    # 최대공약수
    for i in range(max(n, m), 0, -1):
        if m % i == 0 and n % i == 0:
            answer[0] = i
            break
    # 최소공배수
    for i in range(min(n, m), n * m + 1, 1):
        if i % m == 0 and i % n == 0:
            answer[1] = i
            break

    return answer