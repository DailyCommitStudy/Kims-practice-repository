# zip 쓰기 -> 이게 더 빠른듯 (미세하게)
def solution(a, b):
    return sum([i * j for i, j in zip(a, b)])

# 인덱싱으로 하기
def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

## 다른 사람 코드
# lambda를 쓰는 경우
solution = lambda x, y: sum(a*b for a, b in zip(x, y))