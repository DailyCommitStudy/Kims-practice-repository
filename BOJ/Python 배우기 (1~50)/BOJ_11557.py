for _ in range(int(input())) :
    case = dict()
    for i in range(int(input())) :
        n, v = input().split(' ')
        case[int(v)] = n

    print(case[max(case.keys())])

