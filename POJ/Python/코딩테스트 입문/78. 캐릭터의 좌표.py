# 정해진 크기를 벗어날 수 없음.
# board가 11, 11이라면 +-5 까지 이동 가능
# 그러면 up - down, right - left 로 구하고 board 크기에 맞추기

# 결국 if 노가다를 하는 게 답인듯

def solution(keyinput, board):
    answer = [0, 0]
    board = [board[0] // 2, board[1] // 2]
    for i in keyinput:
        if i == 'up' and answer[1] + 1 <= board[1]:
            answer[1] += 1
        elif i == 'down' and answer[1] - 1 >= -board[1]:
            answer[1] -= 1
        elif i == 'left' and answer[0] - 1 >= -board[0]:
            answer[0] -= 1
        elif i == 'right' and answer[0] + 1 <= board[0]:
            answer[0] += 1

    return answer

print(solution(["left", "left", "left", "left", "right", "right", "right", "right"], [5,5]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))