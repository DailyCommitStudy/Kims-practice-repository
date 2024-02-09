## 등차수열의 합 공식 활용

def solution(a, b):
    # a > b일 경우
    if a > b: a, b = b, a
    return (b-a+1)*(a+b)//2

## sum() 활용

def solution(a, b):
    # a > b일 경우
    if a > b: a, b = b, a
    return sum(range(a, b+1))

## 다른 사람의 풀이
# a, b의 대소관계에 크게 신경쓰지 않아도 되는..!
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2