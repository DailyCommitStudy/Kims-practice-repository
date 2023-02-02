for _ in range(int(input())) :
    p = list(map(int, input().split()))[0]
    res = {int(input()) for _ in range(p)}
    print(p-len(res))