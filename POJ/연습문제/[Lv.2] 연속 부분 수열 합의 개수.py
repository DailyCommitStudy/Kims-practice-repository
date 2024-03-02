# 중복되는 값이 있을 수 있기 때문ㅇ ㅔ.... 그냥 직접 구해보는 것이 낫지 않을까

def solution(elements):
    answer = set(elements)  # 1인 연속 부분 수열

    new_elements = elements + elements[:-1]  # 원활한 계산을 위함
    for i in range(2, len(elements)+1): # 연속 부분 집합 길이 2 ~ 5 (1은 answer 정의할 때 넣음)
        for j in range(len(new_elements) - i): # 연속 부분 집합을 만들도록
            answer.add(sum(new_elements[j:j + i]))

    return len(answer)

## 다른 사람의 코드
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)