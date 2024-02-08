n = int(input())

for i in range(n-1, -1, -1) :
    print(' '*i, end='')
    for j in range(n-i) :
        print('*', end=' ')
    print()