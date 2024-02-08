n = int(input())

for i in range(n) :
    for j in range(n) :
        print('*', end=' ')
    print()
    if i % 2 == 0: print(end=' ')