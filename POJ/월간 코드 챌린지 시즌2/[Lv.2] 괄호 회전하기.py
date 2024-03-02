# 회전이라는 게 왼/오로 미는 거네
# 옮겼을 때 첫번째가 (, 즉 괄호 시작지점이면 올바른 것

# 스택 값이 있고, top과 쌍이 맞으면 stack pop
# stack 값이 있고, top과 c가 같은 방향이면 push
# stack 값이 있고, top과 c가 다른 방향일 때 쌍이 맡음 ok 안맞음 X
# stack에 값이 없고, 열린 거면 그냥 push
# stack에 값이 없고, 닫힌 거면 X


def check(s):
    d = {"]": "[", "}": "{", ")": "("}
    stack = []
    s = list(s)
    while s:
        c = s.pop(0)
        if c in d.values():  # 열린 경우 -> push
            stack.append(c)
        else:  # 닫힌 경우
            # stack에 값이 있고, 일치하는 경우 -> stack.pop()
            if stack and stack[-1] == d[c]:
                stack.pop()
            else:  # 그 외 -> 올바르지 않음
                return False
    return False if stack else True


def solution(s):
    n = len(s)
    s += s  # 늘려주기
    answer = 0
    for i in range(n):
        if check(s[i:i + n]):
            answer += 1

    return answer