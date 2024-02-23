# 완주하지 못한 선수의 이름 return
# 동명이인이 있을 수 있다 (중요)
# 1. 미완주자는 동명이인이다
# 2. 미완주자는 동명이인이 아니다
# count를 해서 participant 개수와 completion 개수에서 차이가 나면 return

def solution(participant, completion):
    # 각 이름별로 count
    p, c = {name: 0 for name in participant}, {name: 0 for name in participant}

    for name in participant:
        p[name] += 1

    for name in completion:
        c[name] += 1

    for name in p.keys():
        if p[name] == 0 or p[name] != c[name]:
            return name

# 다른 사람의 코드
# counter 안 써보려고 직접 카운팅한 거긴 했는데
# 이렇게 빼기가 가능하다니? ㄷㄷ 이건 벨로그 쓰면서 검색해보자
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 다른 사람 코드2
# "진짜" 해시함수 사용 예시..! 자료구조 공부하면서 찾아봐야핟ㄹ듯
# 원리는 모르겠다 hash()를 몰라서.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# 다른 사람 코드3
# 와 맞네.. ㅁㅊ... 동명이인도 모두 한번에 검사할 수 있는!! 대단하다
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]