for _ in range(int(input())) :
    sum, avg = 0, 0.0
    for _ in range(int(input())) :
        c, g = map(float, input().split(' '))
        sum += int(c)
        avg += c * g

    print(f'{sum} {round(avg/sum, 1)}')