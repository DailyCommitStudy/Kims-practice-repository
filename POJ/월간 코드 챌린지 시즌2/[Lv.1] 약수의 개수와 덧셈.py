# left부터 right까지 각 수의 약수의 개수.. 각 수의 약수를 빠르게 구할 수 있는 방법?

def func(n):
    res = 0
    for i in range(1, n + 1):
        if n % i == 0:
            res += 1
    return res


def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        if func(n) % 2 == 0:  # 짝
            answer += n
        else:
            answer -= n

    return answer

# 생각해보니 약수는 루트 씌웠을 때 정수면 무조건 홀수 아니면 무조건 짝수잖아?
def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        if int(n ** 0.5) == n ** 0.5:  # 홀
            answer -= n
        else:
            answer += n

    return answer