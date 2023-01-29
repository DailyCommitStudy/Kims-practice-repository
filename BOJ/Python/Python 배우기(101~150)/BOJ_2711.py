for _ in range(int(input())) :
    case = input().split(' ')
    print(case[1][:int(case[0])-1] + case[1][int(case[0]):])