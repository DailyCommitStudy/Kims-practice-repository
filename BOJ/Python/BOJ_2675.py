for _ in range(int(input())) :
    n, s = input().split(' ')
    n = int(n)

    for v in s :
        print(v*n, end='')

    print()