# 숏코드 버전
def solution(x):
    return x%sum(map(int, str(x)))==0

# 재귀함수 활용
def sum_digit(n):
    if n < 10:
        return n
    return n%10 + sum_digit(n//10)

def solution(x):
    return x % sum_digit(x) ==0

## 다른 사람 코드
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0