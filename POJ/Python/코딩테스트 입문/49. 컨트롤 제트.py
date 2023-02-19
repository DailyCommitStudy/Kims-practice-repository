def solution(s):
    answer = 0
    s = s.split(' ')
    for i in range(len(s)) :
        if s[i] == 'Z' :
            answer -= int(s[i-1])
        else : answer += int(s[i])
    return answer

## 2번째 방법
def solution(s):
    answer = list()

    for c in s.split(' '):
        if c == 'Z':
            answer.pop()
        else:
            answer.append(int(c))

    return sum(answer)