# 서로 다른 종류의 수의 최솟값?
# 가장 작은 애부터 빼보거나 가장 큰 애부터 빼보거나 작은 거 큰 거 동시에 빼보던가
# k 각 단계별로 카운트한 값 중 최대값보다 같거나 작으면 1
# k개를 넘어도 됨.

from itertools import combinations


def solution(k, tangerine):
    # 각 단계별 개수 카운트한 결과
    cnt = [tangerine.count(n) for n in set(tangerine)]

    # 하나의 단계만 써도 되는 경우
    if max(cnt) >= k: return 1

    for i in range(2, len(cnt)):
        for j in combinations(cnt, i):
            if sum(j) >= k:
                return i

# 시간 초과.. 쯥
# 챗지피티한테 도움받기
'''
1. cnt 하는 방법. 시간초과의 주 원인은 카운트 중 사용한 count()가 주범이었던 것 같다.
count()가 아니라 get()을 활용해 직접 +=1 해주는 방식을 사용하니 시간이 많이 절약이 되었다,
2. 부분합 구하는 과정에서 슬라이싱을 사용하지 않는 방법
어찌보면 간단하고 기본적인 더 쉬운 코드인데 .. !ㅋㅋ 
얼마나 슬라이싱에 매몰되엇는지알것같은 ㅋㅋ
'''


from itertools import combinations


def solution(k, tangerine):
    # 각 단계별 개수 카운트한 결과 도출 및 정렬
    count_dict = {}
    for n in tangerine:
        count_dict[n] = count_dict.get(n, 0) + 1

    cnt = sorted(count_dict.values(), reverse=True)

    # 하나의 단계만 써도 되는 경우
    if max(cnt) >= k: return 1

    # 부분합 구하는 과정(슬라이싱 X)
    part_sum = 0
    for i, n in enumerate(cnt):
        part_sum += n
        if part_sum >= k:
            return i + 1