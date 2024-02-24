# 소문자, 숫자, -, _, . (.는 처음과 끝 X. 연속 X)'

# 정규표현식을 쓰면 편할 것 같은데..

# 1. 소문자로 치환 lower()
# 2. 특수문자 제거 ~!@#$%^&*()=+[{]}:?,<>/
# 3. 마침표 2개 이상인 곳 하나로
# 4. 마침표 처음이나 끝에 있으면 제거
# 5. 빈 문제열이면 "a"
# 6. 16자 이상이면 첫 15개 빼고 제거 -> 맨 끝이 마침표면 마침표 제거
# 7. 2자 이하면 마지막 문자를 3자가 되도록 반복

# 정직한 코드인듯

import re


def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub(r"[~!@#$%^&*()=+\[{\]}:?,<>/]", "", answer)
    # 3 + 4단계
    sp = answer.split(".")
    for i in range(sp.count("")):
        sp.remove("")
    answer = ".".join(sp)

    # 5단계 + 7단계
    if answer == "":
        return "aaa"

    # 6단계
    if len(answer) >= 16:
        if answer[14] == ".":
            answer = answer[:14]
        else:
            answer = answer[:15]

    # 7단계
    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))

    return answer

## 다른 사람 코드
# 이 코드로 정규식 공부하면 될듯........ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

## 다른 사람 코드2
# 정규식을 안쓴 버전 ㄷㄷ
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer