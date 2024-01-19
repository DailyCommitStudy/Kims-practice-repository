## 너무 모든 경우에 대해서 짜서 잘 모르겠음
# 다시 방법을 생각해볼 필요가 있다..

# 각 위치에 따라 시계, 반시계에 따라 어떻게 계산하는지 수식 찾기
# 1 4 / 3 2 / 2 8 / 2 3
# 북 1 남 2 서 3 동 4
# 동근 / 상점
# 북 1 / 동 4 -> n-d + s
# 북 1 / 서 3 -> d + s
# 남 2 / 동 4 -> n-d + m-s
# 남 2 / 서 3 -> d + m-s

# 북 1 / 남 2 -> (시계) d + s + m (각각 위치가 서, 동 중 어디에 가깝느냐에 따라 다름)
        # -> (반시계) n-d + n-s + m
# 동 4 / 서 3 -> d + s + n
# -> (반시계) m-d + m-s + n
# 같은 방향 -> 절대값(d-s)

# 가로, 세로
n, m = map(int, input().split())
# 각 상점별 위치
store = [tuple(map(int, input().split())) for _ in range(int(input()))]
# 동근이의 위치
d = tuple(map(int, input().split()))

res = 0
for s in store:
    if d[0] == s[0] : res += abs(d[1]-s[1])
    if d[0] == 1 or s[0] == 1:
        if d[0] == 2 or s[0] == 2:
            a = d[1]+s[1]+m
            b = 2 * n - d[1] - s[1] + m
            res += a if a <= b else b
        elif d[0] == 3 or s[0] == 3: res += d[1] + s[1]
        elif d[0] == 4 or s[0] == 4: res += n-d[1]+s[1] #
    if d[0] == 2 or s[0] == 2:
        if d[0] == 3 or s[0] == 3: res += d[1]+m-s[1] #
        elif d[0] == 4 or s[0] == 4: res += n-d[1]+m-s[1]
    if (d[0] == 3 or s[0] == 3) and (d[0] == 4 or s[0] == 4):
        a = d[1] + s[1] + n
        b = 2 * m - d[1] - s[1] + n
        res += a if a <= b else b

print(res)