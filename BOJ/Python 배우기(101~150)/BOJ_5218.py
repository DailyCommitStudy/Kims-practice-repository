for _ in range(int(input())) :
    a, b = input().split(' ')
    print('Distances:', end=' ')
    for i in range(len(a)) :
        aa, bb = ord(a[i])-64, ord(b[i])-64
        if aa <= bb : print(bb-aa, end=' ')
        else : print(bb+26-aa, end=' ')
    print()