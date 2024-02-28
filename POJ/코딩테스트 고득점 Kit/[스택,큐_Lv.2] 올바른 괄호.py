# 전형적인 스택 활용 문제
# 어떻게 푸는 거였지..
# tmp에 뺀 괄호를 넣고
# tmp에 남은 괄호가 없을 때 )ㄱ ㅏ나오면 바로 false

def solution(s):
    tmp = 0
    s = list(s)

    for i in range(len(s)):
        a = s[i]  # pop()은 시간초과 문제로 인덱싱으로 진행

        if a == "(":
            tmp += 1
        elif tmp > 0:  # a == ")", tmp 개수 차감 (매칭)
            tmp -= 1
        else:  # tmp == 0 매칭할 ( X -> 정상적인 경우가 아님
            return False

    # 반복문을 모두 돌아도 ( 개수가 해소되지 않음
    if tmp > 0:
        return False
    else:
        return True