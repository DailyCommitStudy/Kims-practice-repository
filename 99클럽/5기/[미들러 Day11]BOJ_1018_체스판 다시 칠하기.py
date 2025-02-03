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


# 8*8 배열에서 W의 개수를 세고 64를 뺀 절댓값을 반환 = W와 B 개수 차이
def get_wb_diff(arr):
    cnt = 0
    for a in arr:
        cnt += a.count("W")
    
    return abs(32-cnt)

N, M = map(int, input().split(' '))
board = [list(input()) for _ in range(N)]
diffs = []

for i in range(0, N-7): # i ~ i+7 (i:i+8)
    for j in range(0, M-7): # j ~ j+7 (j:j+8)
        arr = []
        for k in range(8):
            arr.append(board[i+k][j:j+8])
        print_arr(arr)
        diff = get_wb_diff(arr)
        diffs.append(diff)
        if diff == 0: 
            break
        
print(min(diffs))


# 그런데 단순히 B와 W의 총 개수만으로 판단하니니 예제6같은 경우에서 문제가 생긴다..
# 같은 행에 BWBBBWWW 로 되어있으면 실제 답은 +2지만, 단순 합으로 생각하면 0이 나오게 된다..
# 그냥 정말 한 행 한 요소를 방문하여 살펴봐야하는 걸까?
# 일단 그리고 최솟값을 하나의 변수에 넣고 그것도가 값이 커지면 다음으로 넘어가도록 하는 게 맞는 것 같다
# 그냥 전부 제대로 탐색해서 넘어가는 게 최선인 것 같다
# 모르겠다.. 다음에 완전탐색을 제대로 공부하고 풀어보고싶다....

N, M = map(int, input().split(' '))
board = [list(input()) for _ in range(N)]

for i in range(0, N-7): # 시작점: i ~ i+7 (i:i+8)
    for j in range(0, M-7): # 시작점: j ~ j+7 (j:j+8)
        for x in range(8):
            for y in range(8):