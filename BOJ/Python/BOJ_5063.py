# 광고를 해야하는 경우(advertise): e-c > r
# 하지 말아야할 경우(do not advertise): e-c < r
# 상관 없는 경우(does not matter): e-c == r

for _ in range(int(input())) :
    r, e, c = map(int, input().split())

    if e-c > r : print('advertise')
    elif e-c < r : print('do not advertise')
    else: print('does not matter')
