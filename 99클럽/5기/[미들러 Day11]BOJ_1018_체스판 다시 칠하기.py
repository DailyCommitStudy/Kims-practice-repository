def print_arr(arr):
    print()
    for a in arr:
        print(''.join(a))
    print()

# 8 * 8 체스판으로 만든다
# 8 * 8 로 자르고, 잘못된 색을 칠한다
# 그러면 8 * 8 로 자를 때, B와 W 비율이 거의 같아야 한다 -> 다시 칧해야 하는 최소 개수가 나옴
# 그 최솟값으로 몇개를 채워야 하는지 알 수 있지 않을까? 
# 아니그냥 8*8로 잘라봤을 때, B와 W의 개수를 세고, 그것이 최소인 절 찾는 거지
# 그러면 2차원 배열을 8*8의 판으로 탐색하고 생각하면서 B와 W의 차이를 배열에 기록하고, 그 최솟값을
# 반환한다. 만약 0이 나오면 바로 끝내고 반환한다. 


# 그런데 단순히 B와 W의 총 개수만으로 판단하니니 예제6같은 경우에서 문제가 생긴다..
# 같은 행에 BWBBBWWW 로 되어있으면 실제 답은 +2지만, 단순 합으로 생각하면 0이 나오게 된다..
# 그냥 정말 한 행 한 요소를 방문하여 살펴봐야하는 걸까?
# 일단 그리고 최솟값을 하나의 변수에 넣고 그것도가 값이 커지면 다음으로 넘어가도록 하는 게 맞는 것 같다
# 그냥 전부 제대로 탐색해서 넘어가는 게 최선인 것 같다
# 모르겠다.. 다음에 완전탐색을 제대로 공부하고 풀어보고싶다....

# N, M = map(int, input().split(' '))
# board = [list(input()) for _ in range(N)]

# for i in range(0, N-7): # 시작점: i ~ i+7 (i:i+8)
#     for j in range(0, M-7): # 시작점: j ~ j+7 (j:j+8)
#         for x in range(8):
#             for y in range(8):


'''
일단 첫번째 줄이 블랙 체스판인 경우 (BWBWBW ...)
그리고 화이트 체스판인 경우 (WBWBWB ... )
두 가지를 구해서 비교한 뒤 더 작은 걸 채택
블랙 체스판을 만들기 위한 비용과 화이트 체스판을 만들기 위한 비용은 서로를 통해 구할 수 있음
블랙 체스판을 만들기 위한 비용이 10일 때, 화이트 체스판을 만들기 위한 비용은 64-10 = 54가 됨
둘 중 하나를 먼저 구하고 계산하면 된다..!

화이트 체스판을 만들기 위한 건 어떻게 구할까..
짝수(0, 2, 4, 6) : WBWBWBWB
홀수(1, 3, 5, 7): BWBWBWBW

비교하자
'''

N, M = map(int, input().split(' '))
board = [list(input()) for _ in range(N)]

w1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
w2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

min_cnt = None
for i in range(0, N-7): # 시작점: i ~ i+7 (i:i+8)
    for j in range(0, M-7): # 시작점: j ~ j+7 (j:j+8)
        cnt = 0
        for x in range(8):
            for y in range(8):
                if x%2: # 홀수
                    if board[i+x][j+y] != w2[y]:
                        cnt += 1
                else: # 짝수
                    if board[i+x][j+y] != w1[y]:
                        cnt += 1

        cnt = min(cnt, 64-cnt) # 블랙 체스판 vs 화이트 체스판 중 비용이 적은 것

        if min_cnt is None or min_cnt > cnt: # 최솟값 갱신
            min_cnt = cnt

print(min_cnt)
