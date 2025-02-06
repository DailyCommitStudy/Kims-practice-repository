'''
바둑판: 19개 가로줄, 19개 세로줄 (1번부터 19번)

같은 색의 바둑알이 연속적으로 다섯 알이 놓이면 이긴다 (가로, 세로, 대각선)
여섯 알 이상이 연속적으로 놓인 경우는 XX

입력이 바둑판의 상태가 주어졌을 때, 검은색이 이겼는지 흰색이 이겼는지, 아직 결정되지 않았는지 판단
흰: 2 / 검: 1 / X: 0

그러면 왼쪽 위(시작점)부터 훑으면서 가로, 세로, 대각선(오른쪽 위, 오른쪽 아래) 네 가지 경우 검사
가로 5번째 줄(4)부터 대각선 오른쪽 위 방향도 추가 검사
가로 15번째 줄(14)까지 대각선 아래 방향, 세로로 검사

왼쪽위부터 쓱 훑으면서 0이면 넘어가고, 1이거나 2면 검사
검사 방식은 set 적용

근데 여섯 알 이상이 놓인 경우가 애매한 점 .. 
i=5 입장에서는 6알 이상이어서 안됐던 거면  i=7 입장에서는 5알 연속이니까 이긴 것..
아니면 시작점을 모두 저장해두고 아닌 경우는 삭제? 아니근데 그게 되냐?
아니면 조회할 때 조건을 돌이 있는지, 검사할 때 조건을 추가 ..?
'''

board = [list(map(int, input().split())) for _ in range(19)]
winner = None

for i in range(19):
    for j in range(19):
        # 돌이 있는지
        if board[i][j] > 0:
            # 가로 방향 검사(j: 14까지)
            if j <= 14 \
                and all(board[i][j] == board[i][j+k] for k in range(5)) \
                and not (j>0 and (board[i][j] == board[i][j-1])) \
                and not (j<14 and (board[i][j] == board[i][j+5])):

                # print("가로")
                winner = board[i][j]
                print(winner)
                print(i+1, j+1)
                break
            # 세로 방향 검사(i: 14까지)
            if i <= 14 \
                and all(board[i][j] == board[i+k][j] for k in range(5)) \
                and not (i>0 and (board[i][j] == board[i-1][j])) \
                and not (i<14 and (board[i][j] == board[i+5][j])):

                # print("세로")
                winner = board[i][j]
                print(winner)
                print(i+1, j+1)
                break
            # 대각선 오른쪽 위 방향 검사(i:4~18, j: 14까지)
            if i >= 4 and j <= 14 \
                and all(board[i][j] == board[i-k][j+k] for k in range(5)) \
                and not (i<18 and j>0 and (board[i][j] == board[i+1][j-1])) \
                and not (i>4 and j<14 and (board[i][j] == board[i-5][j+5])):

                # print("대각선 위")
                winner = board[i][j]
                print(winner)
                print(i+1, j+1)
                break
            # 대각선 아래, 세로 검사(i:0~14, j:14까지)
            if i <= 14 and j <= 14 \
                and all(board[i][j] == board[i+k][j+k] for k in range(5)) \
                and not (i>0 and j>0 and (board[i][j] == board[i-1][j-1])) \
                and not (i<14 and j<14 and (board[i][j] == board[i+5][j+5])):
            
                # print("대각선 아래")
                winner = board[i][j]
                print(winner)
                print(i+1, j+1)
                break
    if winner:
        break

if winner is None:
    print(0)

###

board = [list(map(int, input().split())) for _ in range(19)]
winner = None

for i in range(19):
    for j in range(19):
        # 돌이 있는지
        if board[i][j] > 0:
            # 가로 방향 검사(j: 14까지)
            # 세로 방향 검사(i: 14까지)
            # 대각선 오른쪽 위 방향 검사(i:4~18, j: 14까지)
            # 대각선 아래, 세로 검사(i:0~14, j:14까지)
            if (j <= 14 \
                and all(board[i][j] == board[i][j+k] for k in range(5)) \
                and not (j>0 and (board[i][j] == board[i][j-1])) \
                and not (j<14 and (board[i][j] == board[i][j+5]))) \
                or (i <= 14 \
                and all(board[i][j] == board[i+k][j] for k in range(5)) \
                and not (i>0 and (board[i][j] == board[i-1][j])) \
                and not (i<14 and (board[i][j] == board[i+5][j]))) \
                or ((i >= 4 and j <= 14) \
                and all(board[i][j] == board[i-k][j+k] for k in range(5)) \
                and not (i<18 and j>0 and (board[i][j] == board[i+1][j-1])) \
                and not (i>4 and j<14 and (board[i][j] == board[i-5][j+5]))) \
                or ((i <= 14 and j <= 14) \ 
                and all(board[i][j] == board[i+k][j+k] for k in range(5)) \
                and not (i>0 and j>0 and (board[i][j] == board[i-1][j-1])) \
                and not (i<14 and j<14 and (board[i][j] == board[i+5][j+5]))) :

                winner = board[i][j]
                print(winner)
                print(i+1, j+1)
                break
    if winner:
        break

if winner is None:
    print(0)