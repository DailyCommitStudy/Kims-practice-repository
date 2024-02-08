# 한 옹알이에 대해서 key에 대해 split + join 과정을 거친다.
# 이때 join한 결과, False('')이면 중단 후 answer + 1
# join할 때, 't'로 하는데 이것은 ''으로 join하면서 y'aya'e -> ye가 되어 맞는 결과가 나올 수 없기 때문이다.

def solution(babbling):
    key = ["aya", "ye", "woo", "ma"] # 발음할 수 있는 것

    answer = 0
    for b in babbling:
        temp = b  # 임시저장
        for k in key:
            temp = 't'.join(temp.split(k))
            if set(temp) == set('t'):   # 't'만 들어있으면 발음할 수 있는 단어이다.
                answer += 1
                break

    return answer

### 다른 사람들의 풀이 - 정규표현식 활용

import re

def solution(babbling):
    # 정규표현식을 사용하여 주어진 문자열이 'aya', 'ye', 'woo', 'ma' 중 하나로 이루어져 있는지 확인하는 패턴을 정의
    # ^ 은 문자열의 시작을 의미. ^ 뒤에 있는 패턴으로 시작해야 한다.
    # (aya|ye|woo|ma) 은 괄호 안에 있는 aya...ma가 대안으로 이 중 하나와 매치되어야 한다.
    # + 은 앞의 괄호 안의 패턴이 최소 한 번 이상 반복되어야 한다.
    # $ 은 문자열의 끝을 의미한다.
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    # 입력된 문자열 리스트를 순회하며 정규표현식에 매치되는 경우 카운터 증가
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt