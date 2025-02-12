'''
N일동안 K종류의 맥주 무료 제공
더 많은 참가자들이 다양한 종류의 맥주를 즐길 수 있도록
하루에 맥주 1병만 받을 수 있고, 이전에 받았던 종류의 맥주는 다시는 받을 수 없다
K종류의 맥주에 선호도와 도수 레벨. 마시는 맥주의 도수 레벨이 간 레벨보다 높으면 맥주병 발병 -> XX
마시는 맥주 N개의 선호도 합이 M 이상이 되도록 한다

선호도 합 M을 채우면서 N개의 맥주를 모두 마실 수 있는 간 레벨의 최솟값

N: 축제가 열리는 기간
M: 채워야 하는 선호도의 합
K: 마실 수 있는 맥주 종류의 수
선호도 v, 도수 레벨 c

그러면 맥주 도수별로 정렬한 뒤, 
1~n개씩 더하면서 M 이상이 나오는 값을 찾으면 되잖아
근데 만약에 N개의 선호도를 를 모두 더해도 M을 만족하지 못하면 -1

근데 그러면 맥주 종류는 k인데 N일동안 마실 수 있으니까
K개의 맥주 중 N개를 골라야 한다 -> 조합? (단 맥주 도수별로 정렬했을 때)
'''

# import itertools

# N, M, K = map(int, input().split())
# # 도수 레벨로 정렬
# beers = sorted([tuple(map(int, input().split())) for _ in range(K)], key=lambda x: x[1])

# def find():
#     for comb in itertools.combinations(beers, N):
#         summary = sum(beer[0] for beer in comb)
#         if M <= summary :
#             return max(beer[1] for beer in comb)

# result = find()
# print(result if result else -1)

## 시간초과 문제 발생. 조합..
'''
우선순위 큐?
1. 도수 레벨을 기준으로 오름차순 정렬
-> 가장 낮은 도수 레벨부터 탐색, 선호도를 고려하여 최적의 맥주 선택
2. 우선순위 큐(최소 힙) 활용
-> 선호도가 높은 N개 맥주를 유지하며 도수 레벨 증가


'''

import heapq

N, M, K = map(int, input().split())
# 도수 레벨로 정렬
beers = sorted([tuple(map(int, input().split())) for _ in range(K)], key=lambda x: x[1])

min_spicy = float('inf')
preference_sum = 0
heap = []

for preference, spicy in beers:
    heapq.heappush(heap, preference)
    preference_sum += preference

    # N개를 초과하면 가장 작은 선호도 제거
    if len(heap) > N:
        preference_sum -= heapq.heappop(heap)
    
    # 딱 N개를 선택한 경우, 선호도 합이 M 이상이면 최소 도수 갱신
    if len(heap) == N and preference_sum >= M: 
        min_spicy = min(min_spicy, spicy)
        break

print(min_spicy if min_spicy != float('inf') else -1)