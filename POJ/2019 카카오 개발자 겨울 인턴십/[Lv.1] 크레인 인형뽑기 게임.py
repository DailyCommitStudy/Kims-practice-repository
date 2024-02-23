# 스택을 활용하면 되는 문제.
# 바구니의 -1과 같으면 pop (answer += 2)
# 입력받는 건 1번째 줄이 0번 arr 이런 식이 아니다..


def solution(board, moves):
    answer = 0
    case = [0]  # -1 인덱스 오류 방지

    # 배열 회전 (행을 moves의 번호로 매칭하기 위해서)
    board = list(zip(*board[::-1]))
    board = [list(tup) for tup in board]

    # 0 삭제 (필요없음)
    for arr in board:
        for i in range(arr.count(0)):
            arr.remove(0)

    for m in moves:
        if board[m - 1]:  # m 위치에 인형이 있다
            doll = board[m - 1].pop()  # 인형 뽑기
            if case[-1] == doll:  # 바구니에 넣으면 인형은 터지는가?
                case.pop()
                answer += 2
            else:
                case.append(doll)

    return answer

# 다른 사람 코드
# 굳이 회전을 안 시킨 경우
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer

# 다른 사람 코드2
# 나랑 흐름 자체는 비슷한데 코드 자체가 비범한 느낌
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a