# 두 가지 배열 속 값을 서로 교차시켜서 곱해야하는 거잖음
# A의 최소 * B의 최대 이런 ㄱ ㅔ가장 최소값이지 않을까?
# => 정답 ㅎㅎ

def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    answer = 0

    for a, b in zip(A, B):
        answer += a * b

    return answer