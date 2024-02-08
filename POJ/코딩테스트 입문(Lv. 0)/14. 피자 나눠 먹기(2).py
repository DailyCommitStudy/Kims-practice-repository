## 첫번째 시도
def solution(n):
    for i in range(1, n+1) :
        if (i * 6)/n == (i * 6)//n : return i

## 두번째 시도(수식 차이)
def solution(n):
    for i in range(1, n+1) :
        if (i * 6)%n == 0 : return i