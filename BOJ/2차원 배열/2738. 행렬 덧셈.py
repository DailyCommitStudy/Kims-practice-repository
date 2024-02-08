## N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# N * M 크기의 행렬 입력받기
N, M = map(int, input().split())
A = [list(map(int, input().split())) for n in range(N)]
B = [list(map(int, input().split())) for n in range(N)]

# 계산 및 출력
for n in range(N):
    for m in range(M):
        print(A[n][m] + B[n][m], end=" ")
    print()