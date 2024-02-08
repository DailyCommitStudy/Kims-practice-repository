N = int(input())*2-1
for i in range(1, N+1, 2) :
    print(' ' * ((N-i)//2) + '*'*i)