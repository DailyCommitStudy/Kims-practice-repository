# 도화지: 100 * 100, 색종이가 도화지 밖으로 나가는 경우는 없다.

# 실제 도화지처럼 100 * 100 배열을 만든다
arr = [[0] * 100 for _ in range(100)]

# 입력받은 좌표를 기반으로 색종이가 붙여질 부분을 1로 만든다
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(10):
        arr[a+i-1][b-1:b+9] = [1]*10

# 최종적으로 합을 구한다
print(sum([sum(arr[i]) for i in range(100)]))