# 5자리면
# 01234 4123 ...
# B를 2번 이어 붙였을 때, 그 결과에 A가 포함되면 A에서 B가 될 수 있다는 뜻이다.
# o'hello'hell
# 몇 번 밀었는지 알 수 있는 지표는..
# 반복문으로, 만약 A가 hello라면 ello(4, ), llo(3), lo, o 가 각각 B의 4번재까지와 매칭되는지 확인한다.

# hello, ohell
# hell [:4], _hell [1(5-4):]
# hel [:3], __hel []

def solution(A, B):
    if A in B+B :
        count = 0
        for i in range(len(A)-1, -1, -1):
            count += 1
            if A[:i] == B[len(A)-i:] :
                return count%len(A)
    else :
        return -1

### 다른 사람 풀이
# 하나는 보고 둘은 못 봤구나.. ^^ 2개를 이어붙였을 때 포함되는지 아닌지는 알았는데
# 이어붙였을 때 A의 위치가 즉 몇 번 미는지가 될 수도 있다는 점을 생각 못했다.

solution=lambda a,b:(b*2).find(a)