def Fact(n) :
    res = 1
    for i in range(1, n+1) :
        res *= i
    return res

def solution(balls, share):
    return Fact(balls) / Fact(balls-share) / Fact(share)