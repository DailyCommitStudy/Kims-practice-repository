'''
크기가 N*N인 도시
도시의 각 칸은 빈칸(0), 치킨집(2), 집(1) 중 하나
(r, c) r행 c열 1부터 시작

치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리 = 모든 집의 치킨 거리의 합
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2

도시에 있는 치킨집 중에서 최대 M개를 고름.
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램..
따라서, 도시에 있는 치킨집 중에서 M개에 대한 도시의 치킨 거리의 최솟값을 구하라

집은 h개 있고, 치킨집은 c개가 있을 것
각각의 집은 치킨집별로 거리를 구함

1. 각 집별로 치킨 거리를 구한다
2. 도시의 치킨 거리를 구한다 
3. 도시에 있는 치킨집 위치를 저장해두고 그 중에서 M개를 고르는 경우의 수를 하나씩 가져와서 도시의 치킨거리를 구하고 그 중에서 최솟값을 찾는다

'''

# 도시의 치킨 거리 구하기
# def get_chicken_distance_of_city(stores):
#     chicken_distance_of_city = 0

#     for i in range(N): 
#         for j in range(N):
#             # 집별로 치킨 거리를 구한다
#             if city[i][j] == 1: 
#                 chicken_distance = abs(stores[0][0] - i) + abs(stores[0][1] - j) # 초기값
#                 for store in stores[1:]:
#                     distance = abs(store[0] - i) + abs(store[1] - j)
#                     if chicken_distance > distance:
#                         chicken_distance = distance
                    
#                 chicken_distance_of_city += chicken_distance

#     return chicken_distance_of_city

import itertools 

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨 가게 위치 구하기
chicken_stores = [[i, j] for i in range(N) for j in range(N) if city[i][j] == 2]

min_distance = None
for comb in itertools.combinations(chicken_stores, M):
    chicken_distance_of_city = 0

    for i in range(N): 
        for j in range(N):
            # 집별로 치킨 거리를 구한다
            if city[i][j] == 1: 
                chicken_distance = abs(comb[0][0] - i) + abs(comb[0][1] - j) # 초기값
                for store in comb[1:]:
                    distance = abs(store[0] - i) + abs(store[1] - j)
                    if chicken_distance > distance:
                        chicken_distance = distance
                    
                chicken_distance_of_city += chicken_distance

    if min_distance is None or min_distance > chicken_distance_of_city:
        min_distance = chicken_distance_of_city

print(min_distance)

## 시간 초과 ,,, -> 생각해보니 순열이 아니라 조합으로 풀어야하는데 ㅋㅋ ㅜㅠㅜ 순열을 만드는 함수를 사용하는 바람에 시간 초과가 난 것..
