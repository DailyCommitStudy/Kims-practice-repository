## 첫 번째 시도 -> 시간 초과..
# 같은 알파벳 2개가 붙어있는 경우 제거
# 제거된 뒤 그 앞뒤에 있는 문자가 붙어 짝이 될 수도 있다
# set(s) -> 순회하며 replace(c*2, "")

def solution(s):
    while True:
        past_s = s

        for c in set(s):
            s = s.replace(c * 2, "")

        if past_s == s or s == "":
            break

    return 1 if s == "" else 0

## 두 번쨰 시도 -> 시간 초과
# 다른 로직 -> s 처음부터 -2까지 순회하면서 다음 인덱스와 문자가 같으면 += X
# 문자열의 길이 차제가 너무 길어서 전체를 순회하는 건 비효율적인듯
def solution(s):
    while True:
        past_s = s
        tmp = s[0]

        # s를 처음부터 끝까지 순회하며 연속된 경우 제외
        for c in s[1:-1]:
            if tmp[-1] == c:
                continue
            tmp += c

        s = tmp

        # 변화된 것이 없거나 모두 제거됐으면 break
        if past_s == s or s == "":
            break

    return 1 if s == "" else 0


# 스택을 써라.. (다른 분 코드 참조)
# 내가 두번쨰로 시도했던 것과 유사한 원리
# s의 값들을 순회하며 다른 변수에 넣어둔 마지막 값과 현재 보고 있는
# 문자가 같으면(stack이 비지 않았다면) pop() 후 continue..
# 아.. 어렵네.. 어찌보면 전형적인 스택 문제였던 것 같다

def solution(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue

        stack.append(c)

    return 0 if stack else 1