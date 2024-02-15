# 소수인지 아닌지 확인할 수 있는 방법은 오로지 나눠보는 것
'''
1부터 n까지 숫자 중 소수를 알아낸다.
소수의 개수를 최대 n-1개(1은 소수가 아님)라고 하고,
반복문을 돌면서 각 수가 소수인지 아닌지 확인한다.
1, 본인 외 숫자로 나눠지면 소수가 아니므로 그런 수를 찾으면 1씩 차감한다.
'''
# 로직 자체는 맞으나.. 시간 초과 문제가 있다. 어떻게 할 수 있을지.
# 검사 범위를 절반으로 줄여봐도 시간 초과가 발생했다
# 다른 알고리즘을 찾아볼 필요가 있다.

def solution(n):
    answer = n - 1

    for i in range(4, n + 1):
        for j in range(2, i // 2 + 1):
            # 나눠지면 소수가 아니다
            if i % j == 0:
                answer -= 1
                break

    return answer

# 에라토스테네스의 체 활용
# 성공~
def solution(n):
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:  # i는 소수인가?
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return sum(a)

# 다른 사람의 코드
'''
에라토스테네스의 체를 범위의 숫자가 담긴 set로 구현했다.
그리고 배수를 삭제할 때, 또다른 for문을 통해 각각 삭제하는 것이 아니라
range를 통해 i의 배수가 담긴 집합을 만들어 집합에서 집합을 뺐다

에라토스테네스를 막 공부한 참인지라 다양한 구현방법은 알지 못했는데
이렇게 구현할 수도 있구나! 하는 생각이 들었다.

코멘트를 보니 간단해 좋아 보이는 코드는 맞으나
차집합 연산 시 매번 num 전체를 읽기때문에 내가 짠 것처럼 리스트를 이용하는 것이
속도와 메모리 효율 모두 좋다는 코멘트를 보았다.

각 코드의 테스트 결과를 확인해 보니 리스트를 활용한 것이 훨씬 효율적이라는 것을 확인할 수 있었다.
시간복잡도, 메모리 측면에서 아쉬운 코드지만, 에라토스테네스의 체를 이와같이 활용할 수 있다는 점은 충분히 공부가 되었다.
 '''

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

def solution(n):
    num=set(range(2,n+1))

    for i in range(4,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)