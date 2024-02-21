# 내 가 푼 코드
def solution(x, n):
    try:
        return list(range(x, x*n-1,x)) if x<0 else list(range(x, x*n+1,x))
    except ValueError: # range 함수에 0을 넣으면 오류가 나므로
        return [x] * n

print(solution(0, 10))

# 다른 사람으 ㅣ코드
# 너무 복잡하게 생각했다 내가 ...................ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# 아 바본가 ㅋ
def solution(x, n):
    return [i * x + x for i in range(n)]