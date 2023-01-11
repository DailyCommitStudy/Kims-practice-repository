H, M = map(int, input().split())

if (M < 45) :
    M = 60 + M - 45
    if (H < 1) : H = 24 + H - 1
    else: H -= 1
else :
    M -= 45

print(H, M)