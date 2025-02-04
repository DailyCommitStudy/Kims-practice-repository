'''
완전 탐색 문제
N * M 중 작은 수를 N이라고 할 때, N * N 정사각형부터 2 * 2 정사각형까지 완전탐색
정사각형의 행 길이 n: N ~ 2
왼쪽 위 끝점 설정 i: 0 ~ N-1 / j: 0 ~ M-1
[i][j], [i+n-1][j]
[i][j+m-1], [i+n-1][j+m-1]
3(0~2) * 5(0~4)
3 * 3
0 + 3 - 1

성공!
메모리 109544KB 100ms
'''

def func():
    N, M = map(int, input().split(' '))
    case = [list(input()) for _ in range(N)]

    for n in range(min(N, M), 1, -1): # 정사각형 행 길이
        for i in range(N-n+1):
            for j in range(M-n+1):
                if (case[i][j] == case[i+n-1][j]) and (case[i][j] == case[i][j+n-1]) and (case[i+n-1][j] == case[i+n-1][j+n-1]):
                    return n*n
    
    return 1   # 끝까지 못 찾는 경우

print(func())