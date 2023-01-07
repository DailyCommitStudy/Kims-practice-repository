for _ in range(int(input())) :
    case = input().split()
    res = float(case.pop(0))

    for v in case :
        if (v == "@") :
            res *= 3
        elif (v == "%") :
            res += 5
        elif (v == "#") :
            res -= 7

    print("{:.2f}".format(res))