def solution(board):
    # 1. 2차원 for문을 돌면서 위험지역 표시 후 count
    # 주위를 다 위험지역(1)로 치환해야함.
    # (x-1,y-1)(x-1,y)(x-1,y+1)(x,y-1)(x,y+1)(x+1,y-1)(x+1,y)(x+1,y+1)

    result = [arr[:] for arr in board]

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        try:
                            if i == -1 or j == -1: continue
                            result[i][j] = 1
                        except:
                            continue
    answer = 0
    for r in result:
        answer += r.count(0)

    return answer