# 1) 1 2 3 4 5 ...
# 2) 2 1 2 3 2 4 2 5 ...
# 4) 3 3 1 1 2 2 4 4 5 5 ...

def solution(answers):
    s1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    cnt = [0, 0, 0]
    for a, f, s, t in zip(answers, s1, s2, s3):
        if a == f:
            cnt[0] += 1
        if a == s:
            cnt[1] += 1
        if a == t:
            cnt[2] += 1

    # 가장 많이 맞힌 사람 찾기
    return [i+1 for i, n in enumerate(cnt) if n == max(cnt)]

print(solution([1,1,1,1,1,1]))

# 다른 사람의 풀이
# 나와 비슷하지만 각 학생의 답 패턴을 계산하는 방식이 다름
# 이 코드가 간결해 보이긴 하지만 매 반복마다 idx%len(pattern1) 이 있어서 메모리 측면에서는
# 내 코드가 아쉬울 순 있지만 시간복잡도 면에서는 더 낫지 않을까 싶기도.. 아닌가?
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# 다른 사람 코드2
# 와.. 각 패턴을 리스트에 넣어서 enumerate로 깔끔하게 풀 수 있도록 만들었다
# 대단한데..?

def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

# 다른 사람 코드3
# cycle이란 함수를 처음 봤따 미친..ㄷㄷ
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]