# 세로로 하나 세우기 -> 1칸 차지
# 가로로 두개 겹쳐서 세우기 -> 2칸 차지
# n = 1 -> 1가지
# n = 2 -> 2가지
# n = 3 -> 3가지
# n = 4 -> 5가지
# n = 5 -> 8가지
# 피보나치수열같은데??

def solution(n):
    answer, tmp = 1, 1
    if n <= 2:
        answer = n
    else:
        for i in range(1, n):
            answer, tmp = answer + tmp, answer

    return answer % 1000000007

## 다른 사람의 코드
def tiling(n):
    a,b=1,1
    for i in range(n):a,b=b,a+b
    return a%100000