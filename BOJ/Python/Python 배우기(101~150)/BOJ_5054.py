## 가장 빠른 방법 = 가장 끝에 있는 곳에 차를 대고, 끝까지 걸어갔다가 돌아오는 것
# 즉 a, b, c, d 라면 a에 차를 대는 것. (d-a)*2

for _ in range(int(input())) :
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    print((a[0]-a[-1])*2)


