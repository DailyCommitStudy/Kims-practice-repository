for _ in range(int(input())) :
    case = input().split("X")
    res = 0

    for s in case :
        if s == '' : continue
        res += len(s) * (len(s) + 1) // 2

    print(res)