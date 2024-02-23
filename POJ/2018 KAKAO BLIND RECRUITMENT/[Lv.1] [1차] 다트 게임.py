# 기회별, 1 ~ 10점
# S D T
# *: 해당 점수, 바로 전에 얻은 점수 각 2배
# 스타상은 중첩 가능
# #: 해당 점수 마이너스
# *, # 중첩 가능. 중첩됐을 때는 -2배

# 각 기회를 배열로 관리
# 입력을 어떻게 처리할까...
# 1 / 2 / 3
# isdigit() 으로

def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    answer = [0]

    idx = 0
    for i, c in enumerate(dartResult):
        if c.isdigit():
            score = int(c)
            idx += 1
            if dartResult[i-1] == '1':
                score = 10
                idx -= 1
        else:
            if c in bonus.keys():
                answer.append(score ** bonus[c])
            elif c == "*":
                answer[idx - 1] *= 2
                answer[idx] *= 2
            else:  # "#"
                answer[idx] *= -1

    return sum(answer)

print(solution("1D2S#10S"))

## 다른 사람 코드
# 골칫거리였던 10을 다른 수로 치완한 뒤 리스트로 만든다. 이때 k를 10으로!
# 그 이후로는 순회하면서 계산 진행
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

## 다른 사람 코드2
# 10처럼 스코어가 1이상, 2이하일 수 있다는 것을 n:i로.??
# 이해는 더 해봐야할듯.
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)