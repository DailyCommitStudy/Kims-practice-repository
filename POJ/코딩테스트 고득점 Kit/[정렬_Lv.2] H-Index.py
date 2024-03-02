## 정석적인 풀이는 아닌듯 애초에 정렬을 안 썼으니 ㅋㅋ

def solution(citations):
    answer = 0

    for h in range(len(citations), 0, -1):
        if len(list(filter(lambda x: x >= h, citations))) >= h: return h

    return 0

## 다른 사람의 풀이
# 와 이게뭐고...
# 이해가.. 안됨.. 정신 멀쩡할 때 볼 것
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
